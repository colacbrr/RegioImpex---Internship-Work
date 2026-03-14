from django.urls import path

from .views import bypass, bypass_list, export_bypass_csv

urlpatterns = [
    path("bypass/", bypass, name="bypass"),
    path("bypass/records/", bypass_list, name="bypass_list"),
    path("bypass/export/", export_bypass_csv, name="bypass_export"),
    path("formular_bypass/", bypass, name="formular_bypass"),
]
