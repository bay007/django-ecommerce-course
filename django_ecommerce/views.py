
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ContactForm

User = get_user_model()


def pagina_casa(request):
    context = {
        "title": "Home",
        "content": "Bienvenidos"
    }

    if request.user.is_authenticated():
        context.update({"premium_content": "PREMIUM"})
    return render(request, "home.html", context)


def pagina_sobre_nosotros(request):
    context = {
        "title": "Sobre nosotros",
        "content": "Estea es una prueba para ecomerce"
    }
    return render(request, "home.html", context)


def pagina_contacto(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contacto",
        "content": "Contactanos para poder ayudarte",
        "form": contact_form
    }

    if contact_form.is_valid():
        # esto yas es un diccionario con la data necesaria
        datos_formulario = contact_form.cleaned_data
        print(datos_formulario)

    return render(request, "contact/view.html", context)
