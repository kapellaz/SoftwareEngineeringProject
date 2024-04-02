""" - configuracoes de aprovacao de quizzes - """
from django.apps import AppConfig


class ReviewQuizConfig(AppConfig):
    """configuracoes de aprovacao de quizzes"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'review_quiz'
