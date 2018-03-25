from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from productos.models import Producto


class ProductoViewList(ListView):
    queryset = Producto.objects.all()
    template_name = "productos/producto_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductoViewList, self).get_context_data(*args, **kwargs)
        print(context)
        return context


class ProductoDetailSlug(DetailView):
    template_name = "productos/producto_detail.html"

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Producto, slug=slug)
