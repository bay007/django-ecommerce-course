from django.db import models
from django.db.models.signals import pre_save
from django_ecommerce.utils import unique_slug_generator
from productos.models import Producto
# Create your models here.


class Tag(models.Model):
    titulo = models.CharField(max_length=120)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    productos=models.ManyToManyField(Producto,blank=True)

    def __str__(self):
        return self.titulo


def my_callback_Tag(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(my_callback_Tag, sender=Tag)
