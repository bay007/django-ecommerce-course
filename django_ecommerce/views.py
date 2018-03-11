from django.http import HttpResponse
from django.shortcuts import render



def pagina_casa(request):
    return HttpResponse("<h1>Hola a todos</h1>")