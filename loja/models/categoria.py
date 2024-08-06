from django.db import models

class Categoria(models.Model):
    nome=models.CharField(max_length=50, verbose_name="Nome da categoria")
    descricao_curta= models.CharField(max_length=50, verbose_name="Descrição simples")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
