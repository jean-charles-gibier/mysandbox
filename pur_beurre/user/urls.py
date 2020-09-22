"""
Routes user
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views
from .forms import CustomAuthenticationForm

from .views import dashboard, register, dashboard_section

urlpatterns = [
    path(r"accounts/", include("django.contrib.auth.urls")),
    path(r'login/',
         views.LoginView.as_view(
             template_name="registration/login.html",
             authentication_form=CustomAuthenticationForm),
         name='login'),
    path(r"register/", register, name="register"),
    path(r"dashboard/", dashboard, name='dashboard'),
    re_path(r"^dashboard/(?P<section>\w+)$",
            dashboard_section,
            name='dashboard_section'),
    path(r'admin/', admin.site.urls),
]
