from django.db import models

class PessoaSexoChoice(models.TextChoices) :
    MASCULINO = 'M', 'Masculino'
    FEMININO = 'F', 'Feminino'

class SexoPetChoice(models.TextChoices):
    MACHO = "M", 'Macho'
    FEMEA = "F", "Femea"

class PorteChoice(models.TextChoices):
    MEDIO = "M", "Medio"
    GRANDE = "G", "Grande"
    PEQUENO = "P", "Pequeno"

class TipoConsulta(models.TextChoices):
    EXAME = "E", "Exame"
    CONSULTA = 'C','Consulta'
    VACINA = "V", "Vacina"