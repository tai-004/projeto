from django.db import models
import os  #maneira simples de usar funcionalidades
import uuid  #identificador único universal 
from django.contrib.auth.models import User


#utilizada para gerar numero aleatorios

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("files", filename)


class File(models.Model):
    file = models.FileField(upload_to=user_directory_path, null=True)
    titulo= models.CharField(max_length=20, null= True)
    texto   = models.TextField(max_length=1000, blank=True, null=True)
    equipe = models.TextField(max_length=200, null=True)
    turma = models.CharField(max_length = 20, null= True)
    curso = models.CharField(max_length = 20, null= True)
    orientador = models.CharField(max_length = 20, null= True)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
         permissions = (("excluir", "editar"),("editar", "editar"), ("criar", "criar"))

    def __str__(self):
        return self.titulo



    
  