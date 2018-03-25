
from django.conf.urls import url
from django.contrib import admin
from .views import ProductoViewList, ProductoDetailSlug
urlpatterns = [
    url(r'(?P<slug>[\w-]+)$', ProductoDetailSlug.as_view()),
    url(r'$', ProductoViewList.as_view()),
]
