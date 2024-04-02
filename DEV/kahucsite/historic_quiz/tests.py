from django.http import Http404
from django.test import TestCase
from users.models import KahUCUser
from quiz.models import Quiz, Option
from test_results.models import Answer
from django.contrib.auth.models import Group
from django.urls import reverse
from .forms import EditQuizzForms

class BaseTest(TestCase):

	def setUp(self):
            user_criador= KahUCUser.objects.create(password='pbkdf2_sha256$390000$ZGb2Lnh3sIWTfzOHzOtoou$sS5NzWm8vUFOtDDFAiFUtE8DFVumtIW7XttUDM0BHA8=', is_superuser= False,username='Editor1',first_name='Bruno',last_name='Sequeira',email='adqveqfveq@vavsvew.com',is_staff=False,is_active=True)
            self.user_sem_permissoes= KahUCUser.objects.create(password='pbkdf2_sha256$390000$ZGb2Lnh3sIWTfzOHzOtoou$sS5NzWm8vUFOtDDFAiFUtE8DFVumtIW7XttUDM0BHA8=', is_superuser= False,username='Editor2',first_name='Bruno',last_name='Sequeira',email='adqveqfveq@vavsvew.com',is_staff=False,is_active=True)
            exec(open('create_kahuc_groups.py').read())
            user_aprovador1= KahUCUser.objects.create(password='pbkdf2_sha256$390000$ZGb2Lnh3sIWTfzOHzOtoou$sS5NzWm8vUFOtDDFAiFUtE8DFVumtIW7XttUDM0BHA8=', is_superuser= False,username='Revisor2',first_name='Bruno',last_name='Sequeira',email='adqveqfveq@vavsvew.com',is_staff=False,is_active=True)
            user_aprovador2= KahUCUser.objects.create(password='pbkdf2_sha256$390000$ZGb2Lnh3sIWTfzOHzOtoou$sS5NzWm8vUFOtDDFAiFUtE8DFVumtIW7XttUDM0BHA8=', is_superuser= False,username='Revisor3',first_name='Bruno',last_name='Sequeira',email='adqveqfveq@vavsvew.com',is_staff=False,is_active=True)
            user_aprovador3= KahUCUser.objects.create(password='pbkdf2_sha256$390000$ZGb2Lnh3sIWTfzOHzOtoou$sS5NzWm8vUFOtDDFAiFUtE8DFVumtIW7XttUDM0BHA8=', is_superuser= False,username='Revisor4',first_name='Bruno',last_name='Sequeira',email='adqveqfveq@vavsvew.com',is_staff=False,is_active=True)
            creator_group = Group.objects.get(name='Reviewer')
            user_aprovador1.groups.add(creator_group)
            user_aprovador2.groups.add(creator_group)
            user_aprovador3.groups.add(creator_group)
            self.quiz1 = Quiz.objects.create(id=1,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=user_criador,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False)
            self.edit = reverse('edit_quiz', kwargs={'pk_quiz': self.quiz1.id})
            return super().setUp()

class PermissionsTest(BaseTest):

    def test_edit_test_without_permission(self):
        #testa se o utilizador sem permissão consegue editar um quiz
        self.client.force_login(self.user_sem_permissoes)
        self.quiz1.description = 'Português'
        self.quiz1.question = 'Como se escreve joao?'
        self.quiz1.save()
        response = self.client.post(self.quiz1.id)
        self.assertEqual(response.status_code, 404)
        
