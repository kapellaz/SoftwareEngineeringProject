from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.urls import reverse
from quiz.models import Quiz, Option
from users.models import KahUCUser
from review_quiz.models import Comment,CommentOption
from django.contrib.auth.models import Group


class BaseTest(TestCase):
    def setUp(self):
        #preparar os URL
        #self.review_quiz = reverse('Review a Quiz')
        self.list = reverse('Lista Quizzes a Aprovar')
        self.list_older = reverse ('Lista quizzes a Aprovar por ordem')
        self.list_editados = reverse ('Lista quizzes que ja foram editados')
        self.list_aprovados = reverse ('Lista quizzes que eu aprovei')
        #cria os grupos de permições
        exec(open('create_kahuc_groups.py').read())
        #users com permissão
        self.user_no_aprovador= KahUCUser.objects.create(password='pbkdf2_sha256$390000$ZGb2Lnh3sIWTfzOHzOtoou$sS5NzWm8vUFOtDDFAiFUtE8DFVumtIW7XttUDM0BHA8=', is_superuser= False,username='Revisor1',first_name='Bruno',last_name='Sequeira',email='adqveqfveq@vavsvew.com',is_staff=False,is_active=True)
        user_aprovador1= KahUCUser.objects.create(password='pbkdf2_sha256$390000$ZGb2Lnh3sIWTfzOHzOtoou$sS5NzWm8vUFOtDDFAiFUtE8DFVumtIW7XttUDM0BHA8=', is_superuser= False,username='Revisor2',first_name='Bruno',last_name='Sequeira',email='adqveqfveq@vavsvew.com',is_staff=False,is_active=True)
        user_aprovador2= KahUCUser.objects.create(password='pbkdf2_sha256$390000$ZGb2Lnh3sIWTfzOHzOtoou$sS5NzWm8vUFOtDDFAiFUtE8DFVumtIW7XttUDM0BHA8=', is_superuser= False,username='Revisor3',first_name='Bruno',last_name='Sequeira',email='adqveqfveq@vavsvew.com',is_staff=False,is_active=True)
        user_aprovador3= KahUCUser.objects.create(password='pbkdf2_sha256$390000$ZGb2Lnh3sIWTfzOHzOtoou$sS5NzWm8vUFOtDDFAiFUtE8DFVumtIW7XttUDM0BHA8=', is_superuser= False,username='Revisor4',first_name='Bruno',last_name='Sequeira',email='adqveqfveq@vavsvew.com',is_staff=False,is_active=True)
        creator_group1 = Group.objects.get(name='Creator')
        self.user_no_aprovador.groups.add(creator_group1)
        creator_group2 = Group.objects.get(name='Reviewer')
        user_aprovador1.groups.add(creator_group2)
        user_aprovador2.groups.add(creator_group2)
        user_aprovador3.groups.add(creator_group2)
        #Quiz por ser aprovado
        Quiz.objects.create(id=1,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='À espera de revisão',creator=self.user_no_aprovador,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False)
        Quiz.objects.create(id=2,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.user_no_aprovador,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False)
        self.review = reverse('Review a Quiz', kwargs={'quiz_id': 1})
        return super().setUp()


class URL_test(TestCase):
    def can_access_list1(self):
        response = self.client.get(self.list)
        self.assertEqual(response.status_code, 200)


class no_login_test(BaseTest):
    def test_review_quiz_no_login(self):
        response = self.client.get(self.list_aprovados)
        self.assertEqual(response.status_code, 302)

class PermissionsTest(BaseTest):
    def test_review_test_without_permission(self):
        #testa se o utilizador sem permissão consegue aprovar um quiz
        self.client.force_login(self.user_no_aprovador)
        self.client.post(self.review, format='text/html')
        response = self.client.post(Quiz.objects.filter(id=1).update(num_approvals =+ 1))
        self.assertEqual(response.status_code, 404)
