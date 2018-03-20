from django.views.generic import list, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404

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


class ProductoDetail(DetailView):
    template = "productos/producto_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductoDetail, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        pk = kwargs.get('pk')
        queryset = Producto.objects.obtener_por_id(id=pk)
        if queryset is None:
            raise Http404("No existe este objeto :(")
        return queryset


def producto_detail_view(request, *args, **kwars):
    pk = kwars.get("pk")
    queryset = Producto.objects.obtener_por_id(id=pk)
    if queryset is None:
        raise Http404("No existe este objeto")
    context = {
        'object': queryset
    }
    return render(request, "productos/producto_detail.html", context=context)
