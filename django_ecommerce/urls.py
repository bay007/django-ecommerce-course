"""django_ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import pagina_casa, pagina_contacto, pagina_sobre_nosotros, login, registro, salir
from productos.urls import urlpatterns as productos_url
from busqueda.urls import urlpatterns as busqueda_url
from carritos.urls import urlpatterns as carrito_url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', pagina_casa, name='home'),
    url(r'^contacto/$', pagina_contacto, name='contacto'),
    url(r'^aboutus/$', pagina_sobre_nosotros, name='sobre_nosotros'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', salir, name='salir'),
    url(r'^registro/$', registro, name='registro'),
    url(r'^productos/', include(productos_url, namespace='productos')),
    url(r'^search/', include(busqueda_url, namespace='busqueda')),
    url(r'^carrito/', include(carrito_url, namespace='carrito'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
