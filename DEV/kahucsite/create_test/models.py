from django.db import models
from users.models import KahUCUser
from quiz.models import Tag
from quiz.models import	Quiz

class Teste(models.Model):
	"""Teste que é composto por 20 Quizzes """
	name =models.CharField(max_length=200)
	creator = models.ForeignKey(KahUCUser,null=True,on_delete=models.SET_NULL)
	tags = models.ManyToManyField(Tag)
	quizzes = models.ManyToManyField(Quiz)
