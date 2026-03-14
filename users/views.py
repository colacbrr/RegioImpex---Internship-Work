from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render

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
@user_passes_test(is_admin, login_url="/login/")
def user_list(request):
    query = request.GET.get("q", "").strip()
    users = CustomUser.objects.order_by("username")

    if query:
        users = users.filter(
            Q(username__icontains=query)
            | Q(email__icontains=query)
            | Q(phone_number__icontains=query)
        )

    paginator = Paginator(users, 12)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "user_list.html",
        {
            "page_obj": page_obj,
            "query": query,
        },
    )


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
    return render(request, "profil.html", {"is_admin": is_admin(request.user)})
