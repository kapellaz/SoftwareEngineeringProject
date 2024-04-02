"""classes relativas aos comentarios dos aprovadores - um quiz precisa de 6 especificos e 1 geral"""
from django.db import models
from quiz.models import Quiz, Option
from users.models import KahUCUser


class Comment(models.Model):
    """comentario geral ao quiz"""
    comment = models.CharField(max_length=512, null=True)
    approval = models.BooleanField(null=True)
    version = models.BooleanField(default=True)
    approver = models.ForeignKey(KahUCUser, null=True, on_delete=models.SET_NULL)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)



class CommentOption(models.Model):
    """comentario de uma opcao especifica do quiz"""
    comment = models.CharField(max_length=512, null=True)
    approver = models.ForeignKey(KahUCUser, null=True, on_delete=models.SET_NULL)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
