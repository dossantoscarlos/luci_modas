from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=20)
    
    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        super().save(*args, **kwargs)
    
    def __str__(self)-> str: 
        return self.nome