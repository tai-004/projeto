
from .forms import UsuarioForm, ServidorForm
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import UsuarioForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import  Group
from .models import Perfil
from braces.views import GroupRequiredMixin

#alunos
class UsuarioCreate(CreateView):
    template_name = "registration/register.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="alunos")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context

#seridor
class ServidorCreate(GroupRequiredMixin, CreateView):
    group_required = u"super_servidor"
    template_name = "registration/register.html"
    form_class = ServidorForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="servidor")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context


#perfil usuario
class PerfilUpdate(UpdateView):
    template_name = "registration/perfil.html"
    model = Perfil
    fields = ["nome_completo", "email",  "telefone", "sexo", "curso"]
    success_url = reverse_lazy("templates")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Meus dados pessoais"
        context["botao"] = "Atualizar"

        return context
