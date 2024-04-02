"""A generic way to define our routes."""
from django.urls import path
from . import views
app_name = "quiz"

urlpatterns = [
    path('', views.CreateQuizz, name="Create a Quiz"),
    path('export_xml/', views.export_xml_site, name="Export Quizzes"),
]
