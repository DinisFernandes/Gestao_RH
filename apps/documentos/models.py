from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario

# Create your models here.

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.funcionario_id])


    def __str__(self):
        return self.descricao