
from django.conf.urls import url
from django.contrib import admin
from .views import carrito_home, carrito_add, carrito_remove
urlpatterns = [
    url(r'^add/(?P<id>\d+)$', carrito_add, name="add"),
    url(r'^remove/(?P<id>\d+)$', carrito_remove, name="remove"),
    url(r'$', carrito_home, name="home"),
]
