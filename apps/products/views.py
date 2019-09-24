from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/products_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(self.get_queryset(), slug=kwargs['slug'])
        context = {'object': product}
        return render(request, self.template_name, context)
