from django.db import models

from formacao.models import Formacao
# Create your models here.

class Medico(models.Model):
    name = models.CharField(max_length=255)
    crm = models.CharField(max_length=11)
    formacao=models.ForeignKey(Formacao,on_delete=models.CASCADE)