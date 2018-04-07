from django.db import models
from carritos.models import Carrito
# Create your models here.


class Orden(models.Model):
    CREADA = 'creada'
    PAGADA = 'pagada'
    ENVIADA = 'enviada'
    REEMBOLSADA = 'reembolsada'

    ESTADOS_ORDENES = ((CREADA, 'Creada'), (PAGADA, 'Pagada'),
                       (ENVIADA, 'Enviada'), (REEMBOLSADA, 'Reembolsada'))

    order_id = models.CharField(max_length=120, blank=True)
    carrito = models.ForeignKey(Carrito)
    estado = models.CharField(
        max_length=20, choices=ESTADOS_ORDENES, default=CREADA)
    total_envio = models.DecimalField(
        default=99, decimal_places=2, max_digits=50)
    total = models.DecimalField(default=0, decimal_places=2, max_digits=50)

    def __str__(self):
        return self.order_id
