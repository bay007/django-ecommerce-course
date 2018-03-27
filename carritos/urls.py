
from django.conf.urls import url
from django.contrib import admin
from .views import carrito_home
urlpatterns = [
    url(r'$', carrito_home, name="home"),
]
