import uuid

from datetime import datetime

from django.db import models

from loja.models.cliente import Cliente
from loja.choices import StatusChoice

class Pedido(models.Model):
    codigo = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, verbose_name='Código')
    data = models.DateTimeField(verbose_name="Data da venda",editable=False, default=datetime.now)
    cliente = models.OneToOneField(Cliente, on_delete=models.RESTRICT)
    data_prevista_entrega = models.DateField(verbose_name="Data prevista de entrega",default=datetime.now)
    status = models.CharField(max_length=1, choices=StatusChoice.choices, default=StatusChoice.PAGO, verbose_name="Status")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.data}"
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
