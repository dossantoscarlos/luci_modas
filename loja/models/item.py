import uuid
from loja.models.pedido import Pedido
from django.db import models
from loja.models.produto import Produto

 

class Item(models.Model):
    codigo = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, verbose_name="Código")
    produto = models.ForeignKey(Produto,on_delete=models.RESTRICT, verbose_name="Produto")
    pedido = models.ForeignKey(Pedido, on_delete=models.RESTRICT, verbose_name="Pedido")
    quantidade = models.IntegerField(default=1, verbose_name="Quantidade")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo}"
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(quantidade__gte=1), name="quantidade_gte_1"),
        ]
