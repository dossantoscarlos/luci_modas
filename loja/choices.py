from django.db import models



class StatusChoice(models.TextChoices):
    PAGO = "C", "ABERTO"
    A_PAGAR = "A", "FECHADO"

class ModeloProdutoChoice(models.TextChoices):
    MASCULINO = "M", "MASCULINO"
    FEMININO = "F", "FEMININO"
    UNISEX = "U", "UNISEX"
