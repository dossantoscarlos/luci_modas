from django.db import models


class PessoaSexoChoice(models.TextChoices) :
    MASCULINO = 'M', 'Masculino'
    FEMININO = 'F', 'Feminino'