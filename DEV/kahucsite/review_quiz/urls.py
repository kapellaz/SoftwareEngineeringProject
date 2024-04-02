"""A generic way to define our routes."""
from django.urls import path
from review_quiz import views

urlpatterns = [
    path('<int:quiz_id>/', views.review_one_quiz, name="Review a Quiz"),
    path('list_quizzes_waiting_for_approval/', views.listar_quizzes_a_aprovar_asc,
         name="Lista Quizzes a Aprovar"),
    path('list_quizzes_waiting_for_approval/oldestfirst/',
         views.listar_quizzes_a_aprovar_ordenados_desc, name="Lista quizzes a Aprovar por ordem"),
    path('list_quizzes_waiting_for_approval/editados/',
         views.listar_quizzes_editados, name="Lista quizzes que ja foram editados"),
    path('list_quizzes_waiting_for_approval/aprovados/',
         views.listar_quizzes_aprovados, name="Lista quizzes que eu aprovei"),
]
