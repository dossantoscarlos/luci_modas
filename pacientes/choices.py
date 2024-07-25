from django.db import models


class PacienteSexoChoice(models.TextChoices) :
    MASCULINO = 'M', 'Masculino'
    FEMININO = 'F', 'Feminino'