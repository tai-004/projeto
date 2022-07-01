from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]
    CURSO_CHOICES = [
        ["Info", "Informática"],
        ["Agro_ind", "Agroindrustria"],
        ["Agro", "Agropecuaria"],
        ["Serv", "servidor"],
        ["Super", "superior"]
    ]
    
    nome_completo = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    telefone = models.CharField(max_length=15, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES,  null=True)
    curso = models.CharField(max_length=10, choices=CURSO_CHOICES,  null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome_completo

    class Meta:
         permissions = (("add", "add"), ("perfil", "perfil"), )
