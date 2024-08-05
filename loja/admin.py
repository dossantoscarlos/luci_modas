from django.contrib import admin
from .models import (
    Produto,
    Pedido,
    Cliente,
    Item,
    TipoProduto,
)

# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo","cor","formatted_preco", 'volume', 'descricao_longa', 'image_tag')
    list_filter = ("tipo", "preco", "nome")
    fieldsets = [
        ("Dados do produto",{
            "fields":["nome", "tipo","cor","image","descricao_longa"]
        }),
        ("Estoque", {
            "fields":["volume"]
        }),
        ("Valor", {
            "fields":['preco']
        })
    ]

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display= ("data", "status", "cliente", "data_prevista_entrega")
    list_filter= ("status", "data_prevista_entrega",)
    search_fields=["cliente__nome", "status", "data_prevista_entrega",]
    fieldsets = [
        ("Dados da venda", {
            "fields":['data_prevista_entrega','cliente',"status"]
        })
    ]

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display= ("nome", "contato",)
    search_fields=["nome", "contato",]
    fieldsets = [
        ("Dados do cliente", {
            "fields":['nome','contato',]
        })
    ]

admin.site.register(Item)
admin.site.register(TipoProduto)
