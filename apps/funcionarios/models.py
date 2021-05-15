from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from apps.empresas.models import Empresa
from apps.departamentos.models import Departamento

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    departamento = models.ManyToManyField(Departamento)

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    def __str__(self):
        return self.nome