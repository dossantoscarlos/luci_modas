from django.db import models

from .choices import PacienteSexoChoice

# Create your models here.


class Paciente(models.Model):
    

    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, null=True)
    rg = models.CharField(max_length=8, null=True)
    sexo = models.CharField( max_length=1, 
        choices=PacienteSexoChoice.choices, 
        default=PacienteSexoChoice.MASCULINO,
    )
    email = models.EmailField(max_length=100)
    tel_contato = models.CharField(max_length=20)
    cns = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
   