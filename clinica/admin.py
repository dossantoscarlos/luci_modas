from django.contrib import admin
# from .models import (
#     Veterinario,
#     Tutor,
#     Pet,
#     Agendamento
# )

# class VeterinarioAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'crm')
#     fieldsets = [
#         ("Dados pessoais", {'fields': ['nome'] }),
#         ("Dados profissionais", { 'fields': ['crm'] })
#     ]

# # Register your models here.
# admin.site.register(Veterinario, VeterinarioAdmin)

# class TutorAdmin(admin.ModelAdmin):
#     list_display = (
#         'nome',
#         'sobrenome',
#         'data_nascimento',
#         'cpf',
#         'sexo',
#         'email',
#         'rg',
#         'tel_contato'
#     )

#     fieldsets = [
#         ("Dados pessoais", {
#             'fields': [
#                 'nome',
#                 'sobrenome',
#                 'data_nascimento',
#                 'sexo',
#             ]
#         }),
#         ("Documentos", {
#             'fields': [
#                 'cpf', 
#                 'rg', 
#             ]
#         }),
#         ("Contato", {
#             'fields': [
#                 'email', 
#                 'tel_contato', 
#             ]
#         }),
#     ]

# admin.site.register(Tutor, TutorAdmin)

# class PetAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'data_nascimento', 'porte', 'tutor')
#     fieldsets = [
#         ("Dados pessoais", {
#             'fields': [
#                 'nome', 
#                 'data_nascimento', 
#                 'porte'
#             ]
#         }),
#         ("Responsável", {
#             'fields': [
#                 'tutor'
#             ]
#         }),
#     ]

# admin.site.register(Pet, PetAdmin)

# class AgendamentoAdmin(admin.ModelAdmin):
#     list_display = ('data', 'tipo_consulta', 'pet', 'veterinario')
#     fieldsets = [
#         ("Dados de agendamento", {
#             'fields': [
#                 'data', 
#                 'tipo_consulta', 
#                 'pet',
#                 'veterinario'
#             ]
#         }),
#     ]

# admin.site.register(Agendamento,AgendamentoAdmin)
