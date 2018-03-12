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
    contact_form = ContactForm()
    context = {
        "title": "Contacto",
        "content": "Contactanos para pdoer ayudarte",
        "form": contact_form
    }
    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get("fullName"))
    return render(request, "contact/view.html", context)
