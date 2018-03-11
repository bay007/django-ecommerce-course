from django.http import HttpResponse
from django.shortcuts import render


def pagina_casa(request):
    return render(request, "home.html")
