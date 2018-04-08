from django.db import models
from django.db.models.signals import pre_save, post_save

from carritos.models import Carrito
from django_ecommerce.utils import unique_generator_order_id
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
    costo_envio = models.DecimalField(
        default=99, decimal_places=2, max_digits=50)
    sub_total = models.DecimalField(default=0, decimal_places=2, max_digits=50)

    def __str__(self):
        return self.order_id


def after_save_carrito(sender, instance, *args, **kwargs):
    carrito_obj = instance
    id_carrito = carrito_obj.id
    total_carrito = carrito_obj.total
    orden = Orden.objects.filter(carrito=id_carrito)
    if orden.count() == 1:
        orden = orden.first()
        orden.sub_total = float(total_carrito)
        orden.save()


post_save.connect(after_save_carrito, sender=Carrito)
