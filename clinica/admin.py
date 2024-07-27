from django.contrib import admin
from .models import Veterinario, Tutor

class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm')
    fieldsets = [
        ("Dados pessoais", {'fields': ['nome'] }),
        ("Dados profissionais", { 'fields': ['crm'] })
    ]


# Register your models here.
admin.site.register(Veterinario, VeterinarioAdmin)
admin.site.register(Tutor)