from django.test import TestCase
from users.models import KahUCUser
from quiz.models import Tag, Quiz, Option
from test_results.models import Answer
from create_test.models import Teste

# Create your tests here.

class HallOfFameTest(TestCase):
    '''Testa a app hall of fame
    '''

    def setUp(self):
        '''Setup da base de dados temporária para os testes
        '''
        # criar user de teste
        self.test_user = KahUCUser.objects.create(
            password='pbkdf2_sha256$390000$ZGb2Lnh3sIWTfzOHzOtoou$sS5NzWm8vUFOtDDFAiFUtE8DFVumtIW7XttUDM0BHA8=',
            is_superuser=False,
            username='Solver1',
            first_name='Test',
            last_name='User',
            email='test_user@student.uc.pt',
            is_staff=False,
            is_active=True,
            number_of_correct_quizzes=11,
            number_of_tests_done=1,
        )
        self.tag_test1 = Tag.objects.create(name='TEST1')
        self.tag_test2 = Tag.objects.create(name='TEST2')

        user_aprovador1 = KahUCUser.objects.create(
            password='pbkdf2_sha256$390000$ZGb2Lnh3sIWTfzOHzOtoou$sS5NzWm8vUFOtDDFAiFUtE8DFVumtIW7XttUDM0BHA8=',
            is_superuser=False,
            username='Revisor2',
            first_name='Bruno',
            last_name='Sequeira',
            email='adqveqfveq@vavsvew.com',
            is_staff=False,
            is_active=True,
        )
        user_aprovador2 = KahUCUser.objects.create(
            password='pbkdf2_sha256$390000$ZGb2Lnh3sIWTfzOHzOtoou$sS5NzWm8vUFOtDDFAiFUtE8DFVumtIW7XttUDM0BHA8=',
            is_superuser=False,
            username='Revisor3',
            first_name='Bruno',
            last_name='Sequeira',
            email='adqveqfveq@vavsvew.com',
            is_staff=False,
            is_active=True,
        )
        user_aprovador3 = KahUCUser.objects.create(
            password='pbkdf2_sha256$390000$ZGb2Lnh3sIWTfzOHzOtoou$sS5NzWm8vUFOtDDFAiFUtE8DFVumtIW7XttUDM0BHA8=',
            is_superuser=False,
            username='Revisor4',
            first_name='Bruno',
            last_name='Sequeira',
            email='adqveqfveq@vavsvew.com',
            is_staff=False,
            is_active=True,
        )

        self.quiz1 = Quiz.objects.create(id=1,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz2 = Quiz.objects.create(id=2,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz3 = Quiz.objects.create(id=3,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz4 = Quiz.objects.create(id=4,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz5 = Quiz.objects.create(id=5,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz6 = Quiz.objects.create(id=6,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz7 = Quiz.objects.create(id=7,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz8 = Quiz.objects.create(id=8,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz9 = Quiz.objects.create(id=9,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz10 = Quiz.objects.create(id=10,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz11 = Quiz.objects.create(id=11,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz12 = Quiz.objects.create(id=12,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz13 = Quiz.objects.create(id=13,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz14 = Quiz.objects.create(id=14,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz15 = Quiz.objects.create(id=15,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz16 = Quiz.objects.create(id=16,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz17 = Quiz.objects.create(id=17,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz18 = Quiz.objects.create(id=18,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz19 = Quiz.objects.create(id=19,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)
        self.quiz20 = Quiz.objects.create(id=20,description='Matemática',question='Quanto é 3+6*8 ?',score=20,num_approvals=0,num_rejections=0,approval_state='Aprovado',creator=self.test_user,approver1=user_aprovador1,approver2=user_aprovador2,approver3=user_aprovador3,creation_date='2022-10-04 10:23:54+02',edited=False,tags=self.tag_test1,)

        test1 = Teste.objects.create(name='TEST1', creator=self.test_user)

        test1.quizzes.add(self.quiz1)
        test1.quizzes.add(self.quiz2)
        test1.quizzes.add(self.quiz3)
        test1.quizzes.add(self.quiz4)
        test1.quizzes.add(self.quiz5)
        test1.quizzes.add(self.quiz6)
        test1.quizzes.add(self.quiz7)
        test1.quizzes.add(self.quiz8)
        test1.quizzes.add(self.quiz9)
        test1.quizzes.add(self.quiz10)
        test1.quizzes.add(self.quiz11)
        test1.quizzes.add(self.quiz12)
        test1.quizzes.add(self.quiz13)
        test1.quizzes.add(self.quiz14)
        test1.quizzes.add(self.quiz15)
        test1.quizzes.add(self.quiz16)
        test1.quizzes.add(self.quiz17)
        test1.quizzes.add(self.quiz18)
        test1.quizzes.add(self.quiz19)
        test1.quizzes.add(self.quiz20)

        test1.tags.add(self.tag_test1)
        test1.tags.add(self.tag_test2)

        correct_option1 = Option.objects.create(quiz=self.quiz1,text='resposta correta',selection=True,justification='certa',)
        correct_option2 = Option.objects.create(quiz=self.quiz2,text='resposta correta',selection=True,justification='certa',)
        correct_option3 = Option.objects.create(quiz=self.quiz3,text='resposta correta',selection=True,justification='certa',)
        correct_option4 = Option.objects.create(quiz=self.quiz4,text='resposta correta',selection=True,justification='certa',)
        correct_option5 = Option.objects.create(quiz=self.quiz5,text='resposta correta',selection=True,justification='certa',)
        correct_option6 = Option.objects.create(quiz=self.quiz6,text='resposta correta',selection=True,justification='certa',)
        correct_option7 = Option.objects.create(quiz=self.quiz7,text='resposta correta',selection=True,justification='certa',)
        correct_option8 = Option.objects.create(quiz=self.quiz8,text='resposta correta',selection=True,justification='certa',)
        correct_option9 = Option.objects.create(quiz=self.quiz9,text='resposta correta',selection=True,justification='certa',)
        correct_option10 = Option.objects.create(quiz=self.quiz10,text='resposta correta',selection=True,justification='certa',)
        correct_option11 = Option.objects.create(quiz=self.quiz11,text='resposta correta',selection=True,justification='certa',)
        correct_option12 = Option.objects.create(quiz=self.quiz12,text='resposta correta',selection=True,justification='certa',)
        correct_option13 = Option.objects.create(quiz=self.quiz13,text='resposta correta',selection=True,justification='certa',)
        correct_option14 = Option.objects.create(quiz=self.quiz14,text='resposta correta',selection=True,justification='certa',)
        correct_option15 = Option.objects.create(quiz=self.quiz15,text='resposta correta',selection=True,justification='certa',)
        correct_option16 = Option.objects.create(quiz=self.quiz16,text='resposta correta',selection=True,justification='certa',)
        correct_option17 = Option.objects.create(quiz=self.quiz17,text='resposta correta',selection=True,justification='certa',)
        correct_option18 = Option.objects.create(quiz=self.quiz18,text='resposta correta',selection=True,justification='certa',)
        correct_option19 = Option.objects.create(quiz=self.quiz19,text='resposta correta',selection=True,justification='certa',)
        correct_option20 = Option.objects.create(quiz=self.quiz20,text='resposta correta',selection=True,justification='certa',)


        Answer.objects.create(test=test1, quiz=self.quiz1, user=self.test_user, option=correct_option1)
        Answer.objects.create(test=test1, quiz=self.quiz2, user=self.test_user, option=correct_option2)
        Answer.objects.create(test=test1, quiz=self.quiz3, user=self.test_user, option=correct_option3)
        Answer.objects.create(test=test1, quiz=self.quiz4, user=self.test_user, option=correct_option4)
        Answer.objects.create(test=test1, quiz=self.quiz5, user=self.test_user, option=correct_option5)
        Answer.objects.create(test=test1, quiz=self.quiz6, user=self.test_user, option=correct_option6)
        Answer.objects.create(test=test1, quiz=self.quiz7, user=self.test_user, option=correct_option7)
        Answer.objects.create(test=test1, quiz=self.quiz8, user=self.test_user, option=correct_option8)
        Answer.objects.create(test=test1, quiz=self.quiz9, user=self.test_user, option=correct_option9)
        Answer.objects.create(test=test1, quiz=self.quiz10, user=self.test_user, option=correct_option10)
        Answer.objects.create(test=test1, quiz=self.quiz11, user=self.test_user, option=correct_option11)
        Answer.objects.create(test=test1, quiz=self.quiz12, user=self.test_user, option=correct_option12)
        Answer.objects.create(test=test1, quiz=self.quiz13, user=self.test_user, option=correct_option13)
        Answer.objects.create(test=test1, quiz=self.quiz14, user=self.test_user, option=correct_option14)
        Answer.objects.create(test=test1, quiz=self.quiz15, user=self.test_user, option=correct_option15)
        Answer.objects.create(test=test1, quiz=self.quiz16, user=self.test_user, option=correct_option16)
        Answer.objects.create(test=test1, quiz=self.quiz17, user=self.test_user, option=correct_option17)
        Answer.objects.create(test=test1, quiz=self.quiz18, user=self.test_user, option=correct_option18)
        Answer.objects.create(test=test1, quiz=self.quiz19, user=self.test_user, option=correct_option19)
        Answer.objects.create(test=test1, quiz=self.quiz20, user=self.test_user, option=correct_option20)



    def test_not_authenticated_quiz(self):
        '''Testa se o user nao autenticado consegue aceder ao endpoint das quizzes
        '''
        response = self.client.get('/halloffame/quiz/')
        self.assertEqual(response.status_code, 200)


    def test_not_authenticated_test(self):
        '''Testa se o user nao autenticado consegue aceder ao endpoint dos testes
        '''
        response = self.client.get('/halloffame/test/')
        self.assertEqual(response.status_code, 200)


    def test_authenticated_quiz(self):
        '''Testa se um user autenticado conssegue aceder ao endpoint dos quizzes
        '''
        self.client.force_login(self.test_user)
        response = self.client.get('/halloffame/quiz/')
        self.assertEqual(response.status_code, 200)


    def test_authenticated_test(self):
        '''Testa se um user autenticado conssegue aceder ao endpoint dos testes
        '''
        self.client.force_login(self.test_user)
        response = self.client.get('/halloffame/test/')
        self.assertEqual(response.status_code, 200)


    def test_bad_tag_404_quiz(self):
        '''Testa se uma tag em query param é interpretada como not found na pagina quizzes
        '''
        response = self.client.get('/halloffame/quiz/?tags=TEST_404')
        self.assertEqual(response.status_code, 404)


    def test_bad_tag_404_test(self):
        '''Testa se uma tag em query param é interpretada como not found na página testes
        '''
        response = self.client.get('/halloffame/test/?tags=TEST_404')
        self.assertEqual(response.status_code, 404)


    def test_with_tag_200_quiz(self):
        '''Testa se passando uma tag existente a página de quizzes é carregada
        '''
        response = self.client.get('/halloffame/quiz/?tags=TEST1')
        self.assertEqual(response.status_code, 200)


    def test_with_tag_200_test(self):
        '''Testa se passando uma tag existente a página de testes é carregada
        '''
        response = self.client.get('/halloffame/test/?tags=TEST1')
        self.assertEqual(response.status_code, 200)


    def test_with_tag_all_quiz(self):
        '''Testa se passando a tag 'ALL' os resultados nao sao filtrados por nenhuma tag em quizzes
        '''
        response = self.client.get('/halloffame/quiz/?tags=ALL')
        self.assertEqual(response.context['tag_id'], None)


    def test_with_unknown_tag_quiz(self):
        '''Testa se passando uma tag desconhecida como query param é devolvido um erro 404
        na pagina de quizzes
        '''
        response = self.client.get('/halloffame/test/?unknown=test')
        self.assertEqual(response.status_code, 404)


    def test_with_unknown_tag_test(self):
        '''Testa se passando uma tag desconhecida como query param é devolvido um erro 404
        na pagina de testes
        '''
        response = self.client.get('/halloffame/test/?unknown=test')
        self.assertEqual(response.status_code, 404)


    def test_with_tag_user_quiz(self):
        '''Testa se passando uma tag o nome do user da query é o correto em quizzes
        '''
        response = self.client.get('/halloffame/quiz/?tags=TEST1')
        self.assertEqual(response.context['users_answers'][0][0], 'Solver1')


    def test_with_tag_answers_quiz(self):
        '''Testa se passando uma tag o número de quizes com aquela tag é o correto em quizzes
        '''
        response = self.client.get('/halloffame/quiz/?tags=TEST1')
        self.assertEqual(response.context['users_answers'][0][1], 20)


    def test_with_tag_user_test(self):
        '''Testa se passando uma tag o nome do user da querry é o correto em testes
        '''
        response = self.client.get('/halloffame/test/?tags=TEST1')
        self.assertEqual(response.context['users_completed'][0][0], 'Solver1')


    def test_with_tag_answers_test(self):
        '''Testa se passando uma tag o número de testes completados
        com aquela tag é o correto em testes
        '''
        response = self.client.get('/halloffame/test/?tags=TEST1')
        self.assertEqual(response.context['users_completed'][0][1], 1)
