"""Models of Quiz app."""
from django.db import models
from users.models import KahUCUser
from django.utils import timezone


class Tag(models.Model):
    """Define as Tags dos quizzes."""

    name = models.CharField(max_length=100)

    def __str__(self):
        """Devolve a sua tag"""
        return self.name


class Quiz(models.Model):
    """Define um quiz, ou seja, uma questão de um teste."""

    question = models.CharField(max_length=200)
    description = models.CharField(max_length=512, default='')
    tags = models.ForeignKey(Tag, null=True, on_delete=models.CASCADE)
    score = models.IntegerField(0)

    # Colocar a true quando for para avaliar,
    # colocar a false quando a opnião do terceiro revisor
    edited = models.BooleanField(default=False)
    creator = models.ForeignKey(KahUCUser, null=True,
                                on_delete=models.SET_NULL,
                                related_name='%(class)s_quizzes_created')
    # Nº de vezes que este quizz pode ser usado nos testes
    uses = models.IntegerField(default=2, null=True)
    # Guarda os aprovadores destinados a este quiz
    approver1 = models.ForeignKey(KahUCUser, null=True,
                                  on_delete=models.SET_NULL, default=None,
                                  related_name='%(class)s_quizzes_first_approved')
    approver2 = models.ForeignKey(KahUCUser, null=True,
                                  on_delete=models.SET_NULL, default=None,
                                  related_name='%(class)s_quizzes_second_approved')
    approver3 = models.ForeignKey(KahUCUser, null=True,
                                  on_delete=models.SET_NULL, default=None,
                                  related_name='%(class)s_quizzes_third_approved')

    num_approvals = models.IntegerField(0)
    num_rejections = models.IntegerField(0)

    # procurar por retirar a data
    creation_date = models.DateTimeField(null=True, default=timezone.now)

    # estado de aprovacao do quiz
    approval_state = models.CharField(max_length=20)

    def muda_estado(self):
        """Altera estado de aprovação do quiz."""
        if self.num_rejections + self.num_approvals == 3:
            if self.num_rejections > 0:
                self.approval_state = 'Reprovado'
            else:
                self.approval_state = 'Aprovado'
        else:
            self.approval_state = 'À espera de revisão'

    def __str__(self):
        """Devolve texto da questão."""
        return self.question


class Option(models.Model):
    """Define uma alínea de opção de resposta de um quiz."""

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    selection = models.BooleanField()
    justification = models.CharField(max_length=512)

    def __str__(self):
        """Devolve texto da opção."""
        return self.text
