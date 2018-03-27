from django.shortcuts import render

# Create your views here.


def carrito_home(request):
    return render(request, 'carritos.html')
