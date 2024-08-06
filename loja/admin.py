from django.contrib import admin
from loja.models.pedido import Pedido
from loja.models.cliente import Cliente
from loja.models.item import Item
from loja.models.categoria import Categoria
from loja.models.produto import Produto

# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria","cor","formatted_preco", 'volume', 'descricao_curta', 'image_tag')
    list_filter = ("categoria", "modelo", "nome")
    fieldsets = [
        ("Dados do produto",{
            "fields":["nome", "categoria", "modelo", "cor", "descricao_curta","image","descricao_longa"]
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

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=("codigo", "pedido", 'produto', 'quantidade')
    fieldsets=[
        ("Dados do item", {
            "fields": ["pedido", 'produto', 'quantidade']
        })
    ]


@admin.register(Categoria)
class TipoProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao_curta",)
    fieldsets = [
        ("Dados do tipo de produto", {
            "fields": ["nome", "descricao_curta",]
        })
    ]

