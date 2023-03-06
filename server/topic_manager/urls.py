from django.urls import path

from . import views

urlpatterns = [
    path("create_new_topic", views.create_new_topic),
]