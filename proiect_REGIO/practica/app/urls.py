from django.urls import path
from .views import bypass

urlpatterns = [
    path('formular_bypass/', bypass, name='formular_bypass'),  # Use 'formular_bypass' here
    # other URL patterns...
]
