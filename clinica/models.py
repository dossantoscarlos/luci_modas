from django.db import models

from .choices import PessoaSexoChoice, SexoPetChoice , PorteChoice

# Create your models here.
class Veterinario(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return self.nome

class Tutor(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, null=True)
    rg = models.CharField(max_length=8, null=True)
    sexo = models.CharField( max_length=1, 
        choices=PessoaSexoChoice.choices, 
        default=PessoaSexoChoice.MASCULINO,
    )
    email = models.EmailField(max_length=100)
    tel_contato = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nome
    
class Pet(models.Model):
    nome = models.CharField(max_length=255)
    sexo = models.CharField(max_length=1, choices=SexoPetChoice.choices, default=SexoPetChoice.MACHO)
    data_nascimento = models.DateField()
    porte = models.CharField(max_length=1, choices=PorteChoice.choices, default=PorteChoice.MEDIO)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nome