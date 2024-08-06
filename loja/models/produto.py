import os

from babel.numbers import format_currency

from django.conf import settings
from django.db import models
from loja.models.categoria import Categoria
from loja.choices import ModeloProdutoChoice
from django.utils.html import format_html



class Produto(models.Model): 
    nome = models.CharField(max_length=100 , verbose_name='Nome')
    preco = models.CharField(max_length=100, verbose_name='Preço')
    volume = models.IntegerField(default=1, verbose_name='Quantidade')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=True, verbose_name='Categoria')
    image = models.ImageField(blank=True, upload_to="images/", verbose_name='Imagem')
    cor = models.CharField(max_length=50, blank=True, verbose_name='Cor')
    
    modelo = models.CharField(max_length=1, 
        choices=ModeloProdutoChoice.choices,
        default=ModeloProdutoChoice.MASCULINO,
        verbose_name="Modelo"
    )

    descricao_curta = models.CharField(max_length=100, blank=True, default="", verbose_name="Descrição")
    descricao_longa = models.TextField(verbose_name="Observação")
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