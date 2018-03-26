from django.shortcuts import render
from productos.models import Producto
from django.views.generic import ListView
# Create your views here.


class SearchProductView(ListView):
    template_name = 'search/search_view.html'

    def get_queryset(self, *args, **kargs):
        search_key = self.request.GET.get('q', None)
        print(search_key)
        if search_key is not None:
            qs_title = Producto.objects.filter(titulo__icontains=search_key)
            qs_description = Producto.objects.filter(
                descripcion__icontains=search_key)
            return qs_title.union(qs_description)

        return Producto.objects.featured()
