from django.contrib.auth.models import AbstractUser

from django.db import models


class KahUCUser(AbstractUser):
    """
    Modelo de utilizador a utilizar na base de dados
    """
    number_of_tests_done = models.IntegerField(default=0)
    number_of_correct_quizzes = models.IntegerField(default=0)

