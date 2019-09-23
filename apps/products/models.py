import hashlib

from django.db import models

# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    NAME = 1
    EXT = 0
    new_filename = filename[::-1]
    print(new_filename)
    name = new_filename.split(".")[NAME]
    ext = new_filename.split(".")[EXT][::-1]
    sha_name = hashlib.sha256(name.encode()).hexdigest()
    return f"products/{sha_name}.{ext}"


class Product(models.Model):
    title = models.CharField("Nombre producto", max_length=120)
    price = models.DecimalField("Precio", max_digits=10, decimal_places=2)
    description = models.TextField("Descripción", max_length=255)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return f"{self.title}-${self.price}"
