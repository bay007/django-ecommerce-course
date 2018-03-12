from django.views.generic import list
from django.shortcuts import render

# Create your views here.
from productos.models import Producto


class ProductoView(list.ListView):
    queryset = Producto.objects.all()
    template = "productos/producto_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductoView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def producto_list_view(request):
    queryset = Producto.objects.all()
    print(queryset)
    context = {
        'qs': queryset
    }
    return render(request, "productos/producto_list.html", context)
