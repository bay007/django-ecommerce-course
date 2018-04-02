from django.db import models
from productos.models import Producto
from django.conf import settings
from django.db.models.signals import m2m_changed
# Create your models here.

User = settings.AUTH_USER_MODEL


class CarritoManager(models.Manager):
    def get_or_new(self, request):
        id_carrito = request.session.get("cart_id", None)
        if request.user.is_authenticated:
            if id_carrito is None:
                new_carrito, created = Carrito.objects.get_or_create(
                    id=id_carrito)
                request.session["cart_id"] = new_carrito.id
            else:
                carritos_ = Carrito.objects.filter(id=id_carrito)
                if carritos_.count() == 1:
                    carrito_obj = carritos_.first()
                    carrito_obj.usuario = request.user
                    carrito_obj.save()
        else:
            new_carrito, created = Carrito.objects.get_or_create(id=id_carrito)
            request.session["cart_id"] = new_carrito.id


class Carrito(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    productos = models.ManyToManyField(Producto, blank=True)
    sub_total = models.DecimalField(
        decimal_places=2, max_digits=8, default=0.00)
    total = models.DecimalField(decimal_places=2, max_digits=8, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CarritoManager()

    def __str__(self):
        return str(self.id)


def calcular_subtotal(sender, instance, action, *args, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        sub_total = 0.0
        for producto in instance.productos.all():
            sub_total += float(producto.precio)

        instance.sub_total = sub_total
        instance.total = float(sub_total)*1.16
        instance.save()


m2m_changed.connect(calcular_subtotal, sender=Carrito.productos.through)
