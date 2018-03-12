from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def pagina_casa(request):
    context = {
        "title": "Hola a todos dudues",
        "content": "Bienvenidos"
    }
    return render(request, "home.html", context)


def pagina_sobre_nosotros(request):
    context = {
        "title": "Sobre nosotros",
        "content": "Estea es una prueba para ecomerce"
    }
    return render(request, "home.html", context)


def pagina_contacto(request):
    contact_form = ContactForm(request.POST)
    context = {
        "title": "Contacto",
        "content": "Contactanos para pdoer ayudarte",
        "form": contact_form
    }

    if contact_form.is_valid():
        # esto yas es un diccionario con la data necesaria
        datos_formulario = contact_form.cleaned_data
        print(datos_formulario)

    return render(request, "contact/view.html", context)
