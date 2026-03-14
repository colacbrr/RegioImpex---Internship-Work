from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import BypassForm

@login_required
def bypass(request):
    if request.method == "POST":
        form = BypassForm(request.POST)
        if form.is_valid():
            bypass = form.save(commit=False)
            bypass.utilizator = request.user
            bypass.save()
            messages.success(request, "Bypass entry created successfully.")
            return redirect("bypass")
    else:
        form = BypassForm()

    return render(request, "formular_bypass.html", {"form": form})
