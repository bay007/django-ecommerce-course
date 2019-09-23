from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField("Nombre producto", max_length=120)
    price = models.DecimalField("Precio", max_digits=10, decimal_places=2)
    description = models.TextField("Descripción", max_length=255)

    def __str__(self):
        return f"{self.title}-${self.price}"
