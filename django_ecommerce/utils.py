from django.utils.crypto import get_random_string
from django.utils.text import slugify


'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''


def unique_generator_order_id(instance):
    default_length = 50
    length = len(instance.order_id)
    if instance.order_id is None or instance.order_id == '' or length < default_length:
        return instance.order_id+get_random_string(default_length-length)

    return instance.order_id


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is None:
        slug = slugify(instance.titulo)
    else:
        slug = new_slug

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=get_random_string(
                5, 'abcdefghijkmnpqrstuvwxyz123456789')
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
