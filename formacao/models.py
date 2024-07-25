from django.db import models

# Create your models here.

class Formacao(models.Model):
    nome = models.CharField(max_length=50)
    descricao_curta = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome