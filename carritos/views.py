from django.shortcuts import render
from .models import Carrito
# Create your views here.


def carrito_home(request):
    id_carrito = request.session.get("cart_id", None)
    print(id_carrito)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:

        if id_carrito is None:
            new_carrito, created = Carrito.objects.get_or_create(id=id_carrito)
            request.session["cart_id"] = new_carrito.id
        else:
            new_carrito = Carrito.objects.filter(
                id=id_carrito).update(usuario=request.user)

    else:
        new_carrito, created = Carrito.objects.get_or_create(id=id_carrito)
        request.session["cart_id"] = new_carrito.id

    return render(request, 'carritos.html')
