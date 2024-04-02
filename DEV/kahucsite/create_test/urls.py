"""A generic way to define our routes."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_test, name="Create a Test"),
]
