
from django.conf.urls import url
from django.contrib import admin
from .views import ProductoView, producto_list_view, producto_detail_view, ProductoDetail
urlpatterns = [
    url('detailf/(?P<pk>\d+)$', producto_detail_view),
    url('(?P<pk>\d+)$', ProductoDetail.as_view()),
    url('listf/$', producto_list_view),
    url('$', ProductoView.as_view()),
]
