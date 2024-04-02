from django.db import models

# users
from users.models import KahUCUser
# quiz
from quiz.models import Quiz, Option
# teste
from create_test.models import Teste
# Create your models here.



class Answer(models.Model):
    """Modelo para associar as perguntas de cada teste
    às suas respostas e ao utilizador que a deu
    """
    # o teste a que a que o quiz pertence
    test = models.ForeignKey(Teste, null=True, on_delete=models.SET_NULL)

    # o quiz a que a resposta pertence
    quiz = models.ForeignKey(Quiz, null=True, on_delete=models.SET_NULL)

    # o user que respondeu à pergunta
    user = models.ForeignKey(KahUCUser, null=True, on_delete=models.SET_NULL)

    # a opcao que foi respondida
    option = models.ForeignKey(Option, null=True, on_delete=models.SET_NULL)
