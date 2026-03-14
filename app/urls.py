from django.urls import path
from .views import bypass

urlpatterns = [
    path("bypass/", bypass, name="bypass"),
    path("formular_bypass/", bypass, name="formular_bypass"),
]
