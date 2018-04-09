from django.shortcuts import redirect, render

from accounts.forms import Loginform
from billing.models import Billing
from ordenes.models import Orden
from productos.models import Producto

from .models import Carrito

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
    context = {'base_extends': 'base2.html', "login_form": Loginform()}
    if 'cart_id' in request.session and request.user.is_authenticated():
        orden_object, created = Orden.objects.get_or_new(request)
        print(orden_object.sub_total)
        if orden_object is None:
            return redirect('carrito:home')
        bulling_profile = Billing.objects.get_or_create(user=request.user)
        print(bulling_profile)
        context.update({
            "orden": orden_object,
            "big_total": orden_object.sub_total+orden_object.costo_envio,
            "billing_profile": bulling_profile
        })
    return render(request, 'carrito_checkout.html', context=context)
