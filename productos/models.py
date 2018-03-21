from django.db import models

# Create your models here.


def path_custom(instance, filename):
    print(instance)
    return 'producto_{0}/{1}'.format(instance.titulo.replace(" ", "_"), filename)


class ProductoQuerySet(models.query.QuerySet):
    def _featured(self):
        return self.filter(featured=True)


class ProductoManager(models.Manager):
    def obtener_por_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def featured(self):
        print(self)
        qs = ProductoQuerySet(Producto, using=self._db)._featured()
        if qs.count() == 1:
            return qs.first()
        return None


class Producto(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=19)
    imagen = models.ImageField(upload_to=path_custom, null=True, blank=True)
    featured = models.BooleanField(default=False)

    objects = ProductoManager()

    def __str__(self):
        return "{}-{}".format(self.titulo, self.precio)
