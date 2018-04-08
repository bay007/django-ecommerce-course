from django.shortcuts import render, redirect
from .models import Carrito
from productos.models import Producto
from ordenes.models import Orden
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


def carrito_checkout(request):
    if 'cart_id' in request.session:
        orden_object, created = Orden.objects.get_or_new(request)
        if orden_object is None or orden_object.sub_total == 0:
            return redirect('carrito:home')
        context = {
            "orden": orden_object,
            "big_total": orden_object.sub_total+orden_object.costo_envio
        }
    return render(request, 'carrito_checkout.html', context=context)
