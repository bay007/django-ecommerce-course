"""djangoecommercecourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.products.urls import urlpatterns as products_urls
from apps.user_secure.urls import urlpatterns as user_secure_urls

from .views import AboutView, ContactView, HomeView, WelcomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(title="Home")),
    path('contact/', ContactView.as_view(title="Contacto")),
    path('welcome/', WelcomeView.as_view(title="Welcome"), name="welcome"),
    path('about/', AboutView.as_view(title="About")),
    path('', include(user_secure_urls)),
    path('', include(products_urls))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
