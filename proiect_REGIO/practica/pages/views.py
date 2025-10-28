# pages/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def root_view(request, *args, **kwargs):
    return render(request, "root.html", {})


@login_required
def formular_bypass_view(request, *args, **kwargs):
    return render(request, "formular_bypass.html", {})

# Only include this if necessary and ensure it's not causing circular imports
@login_required
def navbar_view(request, *args, **kwargs):
    return render(request, "navbar.html", {})
