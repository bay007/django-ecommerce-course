from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from productos.models import Producto

# Create your views here.


class SearchProductView(ListView):
    template_name = 'search/search_view.html'

    def get_queryset(self, *args, **kargs):
        search_key = self.request.GET.get('q', None)
        print(search_key)
        if search_key is not None:
            lookup = Q(titulo__icontains=search_key) | Q(
                descripcion__icontains=search_key) | Q(tag__titulo__icontains=search_key)
            return Producto.objects.filter(lookup).distinct()

        return Producto.objects.featured()
