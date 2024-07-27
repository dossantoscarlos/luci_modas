from django.db import models
from .choices import (ModeloProdutoChoice, StatusChoice)

class Produto(models.Model): 
    nome = models.CharField(max_length=100)
    preco = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=1)
    tipo = models.CharField(max_length=100, blank=True)
    cor = models.CharField(max_length=50, blank=True)
    modelo = models.CharField(max_length=1, 
        choices=ModeloProdutoChoice.choices,
        default=ModeloProdutoChoice.MASCULINO
    )
    descricao_longa = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    data = models.DateField()
    status = models.CharField(max_length=1, choices=StatusChoice.choices, default=StatusChoice.PAGO)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status