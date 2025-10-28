# users/urls.py

from django.urls import path
from .views import profil_view, login_view, add_user, user_list, custom_logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('profil/', profil_view, name='profil'),
    path('add_user/', add_user, name='add_user'),
    path('user_list/', user_list, name='user_list'),
    path('logout/', custom_logout_view, name='logout'),
]
