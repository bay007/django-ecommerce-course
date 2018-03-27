from django.db import models
from productos.models import Producto
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class Carrito(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    productos = models.ManyToManyField(Producto, blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=8, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
