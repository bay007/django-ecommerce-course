from django.http import HttpResponse
from django.shortcuts import render



def pagina_casa(request):
    return HttpResponse("Hola a todos")