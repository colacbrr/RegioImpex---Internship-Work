# pages/urls.py

from django.urls import path
from .views import root_view, formular_bypass_view, navbar_view

urlpatterns = [
    path('', root_view, name='root'),
    path('formular_bypass/', formular_bypass_view, name='bypass'),
    path('navbar/', navbar_view, name='navbar'),  # Ensure this is needed
    path('root', root_view, name='root'),
]
