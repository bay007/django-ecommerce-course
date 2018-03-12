
from django.conf.urls import url
from django.contrib import admin
from .views import ProductoView, producto_list_view
urlpatterns = [
    url(r'listf/$', producto_list_view),
    url(r'$', ProductoView.as_view()),
]
