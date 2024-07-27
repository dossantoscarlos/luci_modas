from django.contrib import admin
from .models import Produto, Venda

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo","cor","preco", 'quantidade', 'descricao_longa')
    fieldsets = [
        ("Dados do produto",{
            "fields":["nome", "tipo","cor","descricao_longa"]
        }),
        ("Estoque", {
            "fields":["quantidade"]
        }),
        ("Valor", {
            "fields":['preco']
        })
    ]

admin.site.register(Produto, ProdutoAdmin)

class VendaAdmin(admin.ModelAdmin):
    list_display= ("data", "status", 'produto')
    fieldsets = [
        ("Dados da venda", {
            "fields":["data", "status", "produto"]
        })
    ]

admin.site.register(Venda,VendaAdmin)