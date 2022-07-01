from django.shortcuts import render, redirect
from .models import File
from .forms import FileUploadModelForm
import os
import uuid
from django.http import  HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


# listagem do
@login_required
def file_list(request):
    files = File.objects.all().order_by("-id")
    return render(request, 'file_upload/file_list.html', {'files': files})

def get_queryset(self):
    
    txt_titulo = self.request.GET.get('titulo')

    if txt_titulo:
        file_list = File.objects.filter(titulo_icontains=txt_titulo)   
    else:
        file_list = File.objects.all

        return file_list
        
@login_required
def handle_uploaded_file(file):
    ext = file.name.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    # file path relative to 'media' folder
    file_path = os.path.join('files', file_name)
    absolute_file_path = os.path.join('media', 'files', file_name)

    directory = os.path.dirname(absolute_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(absolute_file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path


# envio do post create
@login_required
@permission_required('file_upload.criar')
def model_form_upload(request):
    if request.method == "POST":
        form = FileUploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.criado_por = request.user
            form.save()
            return redirect("/file/")
    else:
        form = FileUploadModelForm()

    return render(request, 'file_upload/upload_form.html', {'form': form,
                                                            'heading': 'Upload files with ModelForm'})

@login_required
@permission_required('file_upload.excluir')
def excluir(request, id):
    File.objects.get(pk=id).delete()
    return HttpResponseRedirect("/file/")

@login_required
@permission_required('file_upload.editar')
def editar(request, id):
    
    file = File.objects.get(pk=id)
    form = FileUploadModelForm(instance=file)
    
    if request.method == "POST":
        form = FileUploadModelForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/file/")
    
    context = {
        'form': form,
        'file': file
    }
    
    return render(request, 'file_upload/formEdit.html', context)



def template(request):
    return render(request, 'file_list.html', {})
    
@login_required
def detail(request, id):
    file = File.objects.get(pk=id)
    context = {
        'file': file
    }
    
    return render(request, 'file_upload/detail.html', context)



