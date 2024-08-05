from django.db import models
from django.utils.html import format_html
from .choices import (ModeloProdutoChoice, StatusChoice)
import os 
from django.conf import settings
from babel.numbers import format_currency

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class TipoProduto(models.Model):
    nome=models.CharField(max_length=50, verbose_name="Nome do tipo")
    descricao_curta= models.CharField(max_length=50, verbose_name="Descrição simples")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Tipo de produto"
        verbose_name_plural = "Tipos de produto"

class Produto(models.Model): 
    nome = models.CharField(max_length=100 , verbose_name='Nome do produto')
    preco = models.CharField(max_length=100, verbose_name='Preço')
    volume = models.IntegerField(default=1, verbose_name='Quantidade')
    tipo = models.ForeignKey(TipoProduto, on_delete=models.DO_NOTHING, null=True, verbose_name='Tipo do produto')
    image = models.ImageField(blank=True, upload_to="images/", verbose_name='Imagem do produto')
    cor = models.CharField(max_length=50, blank=True, verbose_name='Cor do produto')
    
    modelo = models.CharField(max_length=1, 
        choices=ModeloProdutoChoice.choices,
        default=ModeloProdutoChoice.MASCULINO,
        verbose_name="Modelo"
    )

    descricao_curta = models.CharField(max_length=100, blank=True, default="", verbose_name="Descrição simples")
    descricao_longa = models.TextField(verbose_name="Descrição longa")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nome

    def image_tag(self) -> str:
        if self.image:
            return format_html('<a href="{}" target="_blank"><img src="{}" width="100" height="50" /></a>'.format(self.image.url, self.image.url))
        return "No Image"
    
    image_tag.short_description = 'Image'

    def image_exists(self) -> bool:
        if self.image:
            return os.path.isfile(os.path.join(settings.MEDIA_ROOT, self.image.name))
        return False
    
    def formatted_preco(self) -> str :
        try:
            preco_float = float(self.preco.replace(',', '.'))
            return format_currency(preco_float, 'BRL', locale='pt_BR')
        except ValueError:
            return "Preço Inválido"

    formatted_preco.short_description = 'Preço Formatado'

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(volume__gte=1),
                name="quantidade do produto"
            )
        ]
    
class Item(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.RESTRICT, verbose_name="Produto")
    quantidade = models.IntegerField(default=1, verbose_name="Quantidade")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.quantidade
    
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(quantidade__gte=1), name="quantidade_gte_1"),
        ]

class Venda(models.Model):
    data = models.DateField(verbose_name="Data da venda")
    status = models.CharField(max_length=1, choices=StatusChoice.choices, default=StatusChoice.PAGO, verbose_name="Status")
    items = models.ManyToManyField(Item, verbose_name="Item")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.produto} - {self.status}"
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

class Encomenda(models.Model):
    data_solicitacao = models.DateField(verbose_name="Data de solicitação")
    data_prevista_entrega = models.DateField(verbose_name="Data prevista de entrega")
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, verbose_name="Pedido")
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, verbose_name="Cliente")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.data_prevista_entrega}"
