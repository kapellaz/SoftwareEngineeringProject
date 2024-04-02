from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from quiz.models import Quiz
from selenium import webdriver

#ALTER USER temp_user_name CREATEDB;
class TestSelectTestView(TestCase):

    def setUp(self):
        User = get_user_model()
        
        #User com permissões
        u1 = User.objects.create(id = 1, username='ZF', is_superuser=True, first_name = 'Zeverinorol', last_name='Felixardo', email='teste@student.uc.pt', is_active=True)
        u1.set_password('teste') #metodo para definir a password passando pelo algoritmo de hashing
        u1.save()
        
        #User sem permissões
        u2 = User.objects.create(id = 2, username='OQ', is_superuser=False, first_name = 'Odete', last_name='Quitéria', email='teste2@student.uc.pt', is_active=True)
        u2.set_password('teste2')
        u2.save()
        
        #Quiz
        Quiz.objects.create(id=1, description='Teste', question='Pergunta de teste', score=20, num_approvals=3, num_rejections=0, approval_state='Aprovado', edited=False)


    def test_user_with_no_permissions(self):
        c = self.client

        print('Logging user without permissions: ' + str(c.login(username='OQ', password='teste2')))
        response = c.get('/solve_test/')
        
        # 403 - user without permissions
        self.assertEqual(response.status_code, 403)
        c.logout()


    def test_user_with_permissions(self):
        c = self.client

        print('Logging user with permissions: ' + str(c.login(username='ZF', password='teste')))
        response = c.get('/solve_test/')
        
        # 200 - sucess
        self.assertEqual(response.status_code, 200)
        c.logout()


