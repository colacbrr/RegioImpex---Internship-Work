from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm
from .models import CustomUser

ADMIN_GROUP = "Administratori"
OPERATOR_GROUP = "Operatori"


def is_admin(user):
    return user.groups.filter(name=ADMIN_GROUP).exists()


@login_required
@user_passes_test(is_admin, login_url="/login/")
def add_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            operator_group, _created = Group.objects.get_or_create(name=OPERATOR_GROUP)
            user.groups.add(operator_group)
            messages.success(request, "New operator account created.")
            return redirect("user_list")
    else:
        form = CustomUserCreationForm()

    return render(request, "add_user.html", {"form": form})

@login_required
def user_list(request):
    users = CustomUser.objects.order_by("username")
    return render(request, "user_list.html", {"users": users})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()

    for field in form.fields.values():
        field.widget.attrs.setdefault("class", "form-control")

    return render(request, "login.html", {"form": form})


def custom_logout_view(request):
    auth_logout(request)
    return redirect("login")

@login_required
def profil_view(request, *args, **kwargs):
    return render(request, "profil.html")
