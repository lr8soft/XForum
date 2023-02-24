from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("regist", views.regist),
    path("login", views.login),
    path("logout", views.logout),
]