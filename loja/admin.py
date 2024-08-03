from django.contrib import admin
from .models import Produto, Venda, Cliente

# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo","cor","preco", 'quantidade', 'descricao_longa', 'image')
    fieldsets = [
        ("Dados do produto",{
            "fields":["nome", "tipo","cor","image","descricao_longa"]
        }),
        ("Estoque", {
            "fields":["quantidade"]
        }),
        ("Valor", {
            "fields":['preco']
        })
    ]
    list_editable = ("tipo", "preco",)
    list_filter = ("tipo", "preco", "nome")

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display= ("data", "status", 'produto')
    fieldsets = [
        ("Dados da venda", {
            "fields":["data", "status", "produto"]
        })
    ]

admin.site.register(Cliente)