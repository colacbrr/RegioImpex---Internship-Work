"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from pages.views import root_view, formular_bypass_view, navbar_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('app.urls')),
    path('', root_view, name='root'),
    path('root/', root_view, name='root'),
    path('formular_bypass/', formular_bypass_view, name='bypass'),
    path('navbar/', navbar_view, name='navbar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
