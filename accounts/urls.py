
from django.conf.urls import url
from django.contrib import admin

from accounts.views import login, registro, salir

urlpatterns_accounts = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', salir, name='salir'),
    url(r'^registro/$', registro, name='registro'),
]
