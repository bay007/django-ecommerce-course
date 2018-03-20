from django.db import models

# Create your models here.


def path_custom(instance, filename):
    print(instance)
    return 'producto_{0}/{1}'.format(instance.titulo.replace(" ", "_"), filename)


class Producto(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=19)
    imagen = models.FileField(upload_to=path_custom, null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.titulo, self.precio)
