from django.http import HttpResponse
from django.shortcuts import render


def pagina_casa(request):
    context = {
        'title': "Hola a todos dudues"
    }
    return render(request, "home.html", context)


def pagina_sobre_nosotros(request):
    context = {
        'title': "Sobre nosotros"
    }
    return render(request, "home.html", context)


def pagina_contacto(request):
    context = {
        'title': "Contacto"
    }
    return render(request, "home.html", context)
