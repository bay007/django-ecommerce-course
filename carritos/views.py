from django.shortcuts import render, redirect
from .models import Carrito
from productos.models import Producto
# Create your views here.


def carrito_home(request):
    carrito_obj = Carrito.objects.get_or_new(request)
    context = {
        'carrito': carrito_obj
    }
    request.session['carito_productos'] = carrito_obj.productos.count()
    return render(request, 'carritos.html', context)


def carrito_add(request, *args, **kwargs):
    id = kwargs.get('id', None)
    if id is None:
        return redirect('carrito:home')
    carrito_obj = Carrito.objects.get_or_new(request)
    prod = Producto.objects.get(id=id)
    carrito_obj.productos.add(prod)
    carrito_obj.save()
    return redirect('carrito:home')


def carrito_remove(request, *args, **kwargs):
    id = kwargs.get('id', None)
    if id is None:
        return redirect('carrito:home')
    carrito_obj = Carrito.objects.get_or_new(request)
    productos = carrito_obj.productos.filter(id=id)
    if productos.count() > 0:
        carrito_obj.productos.remove(productos.first())
        carrito_obj.save()

    return redirect('carrito:home')
