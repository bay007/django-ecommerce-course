from django.shortcuts import render

# Create your views here.


def carrito_home(request):
    id_carrito = request.session.get("cart_id", None)
    if id_carrito is None:
        print("No hay, crear nuevo")
        request.session.__setitem__("cart_id", 12)
    else:
        print("Carrito existe")
    return render(request, 'carritos.html')
