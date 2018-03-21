
from django.conf.urls import url
from django.contrib import admin
from .views import ProductoView, producto_list_view, producto_detail_view, ProductoDetail, producto_list_view_featured
urlpatterns = [
    url(r'detailf/(?P<pk>\d+)$', producto_detail_view),
    url(r'(?P<pk>\d+)$', ProductoDetail.as_view()),
    url(r'listf/$', producto_list_view),
    url(r'listfeatured$', producto_list_view_featured),
    url(r'$', ProductoView.as_view()),
]
