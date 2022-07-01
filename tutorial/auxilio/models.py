from django.db import models
import os
import uuid
from django.contrib.auth.models import User
# Create your models here.
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("auxilio", filename)

class Auxilio(models.Model):
    file = models.FileField(upload_to=user_directory_path, null=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
         permissions = (("aux", "aux"), ("atual", "atual"), ("exc", "exc"))