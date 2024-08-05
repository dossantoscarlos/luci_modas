from django.db import models



class StatusChoice(models.TextChoices):
    PAGO = "C", "PAGO"
    A_PAGAR = "A", "A PAGAR"

class ModeloProdutoChoice(models.TextChoices):
    MASCULINO = "M", "MASCULINO"
    FEMININO = "F", "FEMININO"
    UNISEX = "U", "UNISEX"
