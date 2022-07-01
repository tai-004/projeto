from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Auxilio
from .form import UploaderModelForm
import uuid
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


#listar
@login_required
def file_list(request):
    files = Auxilio.objects.all().order_by("-id")
    return render(request, 'auxilio/file_list.html', {'files': files})

# Criar documentos
@login_required
@permission_required('auxilio.aux')
def uploader(request):
    if request.method == "POST":
        form = UploaderModelForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.criado_por = request.user
            form.save()
            return redirect("/auxilio/")
    else:
        form = UploaderModelForm()

    return render(request, 'auxilio/upload_form.html', {'form': form, 'heading': 'Postar documentos de Auxílio'})


# Enviando pdfs para 'media'
@login_required
def handle_uploaded_file(file):
    ext = file.name.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext)

    file_path = os.path.join('files', file_name)
    absolute_file_path = os.path.join('media', 'files', file_name)

    directory = os.path.dirname(absolute_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(absolute_file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path

#excluir arquivos
@login_required
@permission_required('auxilio.exc')
def excluir(request, id):
    
    Auxilio.objects.get(pk = id).delete()
    
    return HttpResponseRedirect("/auxilio/")

#editar arquivos
@login_required
@permission_required('auxilio.atual')
def editar(request, id):
    auxilio = Auxilio.objects.get(pk = id)
    form = UploaderModelForm(instance=auxilio)
    
    if request.method == "POST":
        form = UploaderModelForm(request.POST, instance=auxilio)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/auxilio/")
    else:    
        form = UploaderModelForm(instance=auxilio)
    
    context = {
        'form': form,
        'auxilio': auxilio
    }
    
    return render(request, 'auxilio/formEdit.html', context)

#detalhar arquivos
def detail(request, id):
    auxilio = Auxilio.objects.get(pk=id)
    context = {
        'auxilio': auxilio
    }
    
    return render(request, 'auxilio/detail.html', context)

def template(request):
    return render(request, 'file_list.html', {})

