from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
# Create your models here.

User = settings.AUTH_USER_MODEL


class Billing(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField()
    active = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '{id}::{user}'.format(user=self.user, id=self.user.id)


def user_created_cerate_billing(sender, instance, *args, **kwargs):
    if kwargs.get('created', False):
        Billing.objects.get_or_create(user=instance, emaiil=instance.email)


post_save.connect(user_created_cerate_billing, sender=User)
