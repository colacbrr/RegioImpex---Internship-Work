# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm
from .models import CustomUser


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Administratori').exists(), login_url='/login/')
def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            operator_group, created = Group.objects.get_or_create(name='Operatori')
            user.groups.add(operator_group)
            return redirect('user_list')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'add_user.html', {'form': form})  # Partea aceasta inca nu este functionala complet/ nu este implementata

@login_required
def user_list(request):
    users = CustomUser.objects.all()  
    return render(request, 'user_list.html', {'users': users}) # Partea aceasta inca nu este functionala complet/ nu este implementata
                                                    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            # Redirect to a valid URL after login
            return redirect('root')  # Redirect to root page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def custom_logout_view(request):
    user = request.user
    auth_logout(request)
    

    # Check user group and redirect accordingly
    if user.groups.filter(name='Administrator').exists():
        return redirect('/admin/login/')  # Redirect to admin logout
    elif user.groups.filter(name='Operator').exists():
        return render(request,"logout.html")
    
    return redirect('login')
  

@login_required
def profil_view(request, *args, **kwargs):
    return render(request, "profil.html", {})