from django.urls import path

from .views import (
    list_quizzs,
    details_quiz,
    edit_quiz,
    )

urlpatterns = [
    path('',list_quizzs, name="list_quizzs"),
    path('quiz=<int:pk_quiz>',details_quiz, name="details_quiz"),
    path('quiz=<int:pk_quiz>/edit', edit_quiz, name="edit_quiz"),

]
