from django.urls import path

from .views import add_user, custom_logout_view, login_view, profil_view, user_list

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", custom_logout_view, name="logout"),
    path("profile/", profil_view, name="profile"),
    path("profil/", profil_view, name="profil"),
    path("users/", user_list, name="user_list"),
    path("users/add/", add_user, name="add_user"),
]
