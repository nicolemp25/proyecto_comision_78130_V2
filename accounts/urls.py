from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import *

urlpatterns = [
    # Login y logout usando las vistas genéricas de Django
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),

    # Registro (crear usuario)
    path("register/", register, name="register"),

    # Vistas del perfil
    path("profile/", profile_detail, name="profile_detail"),
    path("profile/edit/", profile_edit, name="profile_edit"),
]