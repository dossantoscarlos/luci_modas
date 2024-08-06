from django.db import models

class StatusChoice(models.TextChoices):
    PAGO = "C", "ABERTO"
    A_PAGAR = "A", "FECHADO"

class ModeloProdutoChoice(models.TextChoices):
    MASCULINO = "M", "MASCULINO"
    FEMININO = "F", "FEMININO"
    UNISEX = "U", "UNISEX"

class CategoriaChoice(models.TextChoices):
    CALCADO = "C", "Calçado"
    VESTIARIO= "V", "Vestiário"

class SubCategoriaChoice(models.TextChoices):
    CAMISA = 0, "Camisa"
    SAPATO = 1, "Sapato"
    SAIA = 2, "Saia"
    VESTIDO = 3, "Vestido"
    CAMISETA = 4, "Camiseta"
    CASACO = 5, "Casaco"
    JAQUETA = 6, "Jaqueta"
    MOLETON = 7, "Moleton"
    TENIS = 8, "Tenis"