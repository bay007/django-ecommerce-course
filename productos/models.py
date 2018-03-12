from django.db import models

# Create your models here.


class Producto(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=19)
