from django.shortcuts import render
from .models import Carrito
# Create your views here.


def carrito_home(request):
    carrito_obj = Carrito.objects.get_or_new(request)
    return render(request, 'carritos.html')
