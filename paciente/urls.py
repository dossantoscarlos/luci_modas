from django.urls import path

from paciente.views import index


urlpatterns = [
    path('', index),
]