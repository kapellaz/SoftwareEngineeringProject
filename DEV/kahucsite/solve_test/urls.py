"""A generic way to define our routes."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_test_view, name="Select a test"),
    path('temp/<test_id>/', views.test_redirect_view, name="Solving a test"),
    path('<test_id>/<quiz_id>/', views.test_page_view, name="Solving a test"),
]
