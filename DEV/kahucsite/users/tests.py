from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core import mail
from django.test import TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.files.uploadedfile import SimpleUploadedFile

from quiz.models import Quiz, Tag
from .tokens import account_activation_token

User = get_user_model()


class BaseTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.password_reset_email_url = reverse('password_reset')
        self.profile_url = reverse('profile')
        self.import_url = reverse('importxml')
        self.export_url = reverse('quiz:Export Quizzes')
        self.user = {
            'first_name': 'antonio',
            'last_name': 'silva',
            'username': 'testemail@student.uc.pt',
            'password1': '#123456a',
            'password2': '#123456a',
        }
        exec(open('create_kahuc_groups.py').read())
        return super().setUp()


class RegisterMailTest(TestCase):
    def test_send_ucemail(self):
        # Mandar o mail
        mail.send_mail('Ative a sua conta KahUC', 'Mensagem enviada',
                       'from@example.com', ['andre.moreira@student.uc.pt'],
                       fail_silently=False)
        # Testar se o mail foi enviado
        self.assertEqual(len(mail.outbox), 1)
        # Testar se o subject esta correto.
        self.assertEqual(mail.outbox[0].subject, 'Ative a sua conta KahUC')

    def test_send_deiemail(self):
        # Mandar o mail
        mail.send_mail('Ative a sua conta KahUC', 'Mensagem enviada',
                       'from@example.com', ['test@dei.uc.pt'],
                       fail_silently=False)
        # Testar se o mail foi enviado
        self.assertEqual(len(mail.outbox), 1)
        # Testar se o subject esta correto.
        self.assertEqual(mail.outbox[0].subject, 'Ative a sua conta KahUC')

    def test_send_studentdeiemail(self):
        # Mandar o mail
        mail.send_mail('Ative a sua conta KahUC', 'Mensagem enviada',
                       'from@example.com', ['test@student.dei.uc.pt'],
                       fail_silently=False)
        # Testar se o mail foi enviado
        self.assertEqual(len(mail.outbox), 1)
        # Testar se o subject esta correto.
        self.assertEqual(mail.outbox[0].subject, 'Ative a sua conta KahUC')


class RegisterTest(BaseTest):
    def test_can_register(self):
        res = self.client.post(self.register_url, self.user, format="text/html")
        self.assertEqual(res.status_code, 302)

    def test_no_email(self):
        response = self.client.post(self.register_url,
                                    {"username": "", "password1": "asd_asd123", "password2": "asd_asd123"},
                                    format="text/html")
        self.assertEqual(response.status_code, 200)

    def test_no_password(self):
        response = self.client.post(self.register_url,
                                    {"username": "uc12131231@student.uc.pt", "password1": "", "password2": ""})
        self.assertEqual(response.status_code, 200)

    def test_email_wrong_format(self):
        response = self.client.post(self.register_url,
                                    {"first_name": "ola", "last_name": "boas", "username": "uc12131231@gmail.com",
                                     "password1": "asd_asd123", "password2": "asd_asd123"})
        self.assertEqual(response.status_code, 200)

    def test_already_registered(self):
        self.client.post(self.register_url,
                         {"first_name": "ola", "last_name": "boas", "username": "uc12131231@student.uc.pt",
                          "password1": "asd_asd123", "password2": "asd_asd123"})
        response = self.client.post(self.register_url,
                                    {"first_name": "ola", "last_name": "boas", "username": "uc12131231@student.uc.pt",
                                     "password1": "asd_asd123", "password2": "asd_asd123"})
        self.assertEqual(response.status_code, 200)

    def test_short_password(self):
        response = self.client.post(self.register_url,
                                    {"first_name": "ola", "last_name": "boas", "username": "uc12131231@student.uc.pt",
                                     "password1": "asd_123", "password2": "asd_123"})
        self.assertEqual(response.status_code, 200)

    def test_no_number_password(self):
        response = self.client.post(self.register_url,
                                    {"first_name": "ola", "last_name": "boas", "username": "uc12131231@student.uc.pt",
                                     "password1": "asd_asdss", "password2": "asd_asdss"})
        self.assertEqual(response.status_code, 200)

    def test_no_special_password(self):
        response = self.client.post(self.register_url,
                                    {"first_name": "ola", "last_name": "boas", "username": "uc12131231@student.uc.pt",
                                     "password1": "asdaasdss", "password2": "asdaasdss"})
        self.assertEqual(response.status_code, 200)

    def test_correct_password(self):
        response = self.client.post(self.register_url,
                                    {"first_name": "ola", "last_name": "boas", "username": "uc12131231@studen.uc.pt",
                                     "password1": "asd_asd123", "password2": "asd_asd123"})
        self.assertEqual(response.status_code, 200)

    def test_correct_email(self):
        response = self.client.post(self.register_url,
                                    {"first_name": "ola", "last_name": "boas", "username": "uc12131231@student.uc.pt",
                                     "password1": "asdasd123", "password2": "asdasd123"})
        self.assertEqual(response.status_code, 200)

    def test_all_correct(self):
        response = self.client.post(self.register_url,
                                    {"first_name": "ola", "last_name": "boas", "username": "uc12131231@student.uc.pt",
                                     "password1": "asd_asd123", "password2": "asd_asd123"})
        self.assertEqual(response.status_code, 302)

    def test_wrong_2nd_password(self):
        response = self.client.post(self.register_url,
                                    {"first_name": "ola", "last_name": "boas", "username": "uc12131231@student.uc.pt",
                                     "password1": "asd_asd123", "password2": "asd_asd23"})
        self.assertEqual(response.status_code, 200)


class LoginTest(BaseTest):

    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_cantlogin_with_unverified_email(self):
        self.client.post(self.register_url, self.user, format="text/html")
        res = self.client.post(self.login_url, {'password': '#123456a', 'username': 'testemail@student.uc.pt'},
                               format='text/html')
        self.assertEqual(res.status_code, 200)

    def test_login_success(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        response = self.client.post(self.login_url, {'password': '#123456a', 'username': 'testemail@student.uc.pt'},
                                    format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_cantlogin_with_no_username(self):
        response = self.client.post(self.login_url, {'password': 'passwped', 'username': ''}, format="text/html")
        self.assertEqual(response.status_code, 200)

    def test_cantlogin_with_no_password(self):
        response = self.client.post(self.login_url, {'username': 'passwped', 'password': ''}, format="text/html")
        self.assertEqual(response.status_code, 200)

    def test_login_fail(self):
        response = self.client.post(self.login_url, {'username': 'passwped', 'password': 'password'},
                                    format="text/html")
        self.assertEqual(response.status_code, 200)


class NewPasswordTest(BaseTest):

    def test_no_password(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        password_reset_url = reverse('password_reset_confirm',
                                     kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                                             'token': account_activation_token.make_token(user)})
        response = self.client.post(password_reset_url, {'new_password1': '', 'new_password2': '#123456a'},
                                    format="text/html")
        self.assertEqual(response.status_code, 200)

    def test_no_password_confirmation(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        password_reset_url = reverse('password_reset_confirm',
                                     kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                                             'token': account_activation_token.make_token(user)})
        response = self.client.post(password_reset_url, {'new_password1': '#123456a', 'new_password2': ''},
                                    format="text/html")
        self.assertEqual(response.status_code, 200)

    def test_no_password_no_confirmation(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        password_reset_url = reverse('password_reset_confirm',
                                     kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                                             'token': account_activation_token.make_token(user)})
        response = self.client.post(password_reset_url, {'new_password1': '', 'new_password2': ''}, format="text/html")
        self.assertEqual(response.status_code, 200)

    def test_password_less_8_characters(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        password_reset_url = reverse('password_reset_confirm',
                                     kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                                             'token': account_activation_token.make_token(user)})
        response = self.client.post(password_reset_url, {'new_password1': '#12345a', 'new_password2': '#12345a'},
                                    format="text/html")
        self.assertEqual(response.status_code, 200)

    def test_password_less_1_letter(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        password_reset_url = reverse('password_reset_confirm',
                                     kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                                             'token': account_activation_token.make_token(user)})
        response = self.client.post(password_reset_url, {'new_password1': '#1234567', 'new_password2': '#1234567'},
                                    format="text/html")
        self.assertEqual(response.status_code, 200)

    def test_password_no_numbers(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        password_reset_url = reverse('password_reset_confirm',
                                     kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                                             'token': account_activation_token.make_token(user)})
        response = self.client.post(password_reset_url, {'new_password1': '#abcdefg', 'new_password2': '#abcdefg'},
                                    format="text/html")
        self.assertEqual(response.status_code, 200)

    def test_password_no_special(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        password_reset_url = reverse('password_reset_confirm',
                                     kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                                             'token': account_activation_token.make_token(user)})
        response = self.client.post(password_reset_url, {'new_password1': 'abcdefg1', 'new_password2': 'abcdefg1'},
                                    format="text/html")
        self.assertEqual(response.status_code, 200)

    def test_password_confirmation_different(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        password_reset_url = reverse('password_reset_confirm',
                                     kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                                             'token': account_activation_token.make_token(user)})
        response = self.client.post(password_reset_url, {'new_password1': '#123456a', 'new_password2': '123456a#'},
                                    format="text/html")
        self.assertEqual(response.status_code, 200)

    def password_reset_ok(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        password_reset_url = reverse('password_reset_confirm',
                                     kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                                             'token': account_activation_token.make_token(user)})
        response = self.client.post(password_reset_url, {'new_password1': '#123456a', 'new_password2': '#123456a'},
                                    format="text/html")
        self.assertEqual(response.status_code, 302)


class PasswordChangeInsertEmail(BaseTest):

    def test_no_email(self):
        response = self.client.post(self.password_reset_email_url, {'email': ''}, format="text/html")
        self.assertEqual(response.status_code, 200)

    def test_invalid_account(self):
        response = self.client.post(self.password_reset_email_url, {'email': 'testemail1234incorreto@student.uc.pt'},
                                    format="text/html")
        self.assertEqual(response.status_code, 200)

    def test_email_not_verified(self):
        self.client.post(self.register_url, self.user, format="text/html")
        response = self.client.post(self.password_reset_email_url, {'email': 'testemail@student.uc.pt'},
                                    format="text/html")
        self.assertEqual(response.status_code, 200)

    def test_email_correct(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        response = self.client.post(self.password_reset_email_url, {'email': 'testemail@student.uc.pt'},
                                    format="text/html")
        self.assertEqual(response.status_code, 200)


class RecoverPasswordMailTest(BaseTest):

    def test_password_send_ucemail(self):
        mail.send_mail('Recupere a sua password', 'Mensagem enviada',
                       'from@example.com', ['ecarvalho@student.uc.pt'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Recupere a sua password')

    def test_password_send_deiemail(self):
        mail.send_mail('Recupere a sua password', 'Mensagem enviada',
                       'from@example.com', ['test@dei.uc.pt'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Recupere a sua password')


class UserPageTests(BaseTest):
    def test_can_acess_user_page(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        self.client.post(self.login_url, {'password': '#123456a', 'username': 'testemail@student.uc.pt'},
                         format='text/html')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)

    def test_can_acess_import_XML(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        self.client.post(self.login_url, {'password': '#123456a', 'username': 'testemail@student.uc.pt'},
                         format='text/html')
        self.client.get(self.profile_url)
        response = self.client.get(self.import_url)
        self.assertEqual(response.status_code, 200)

    def test_can_acess_export_XML(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        self.client.post(self.login_url, {'password': '#123456a', 'username': 'testemail@student.uc.pt'},
                         format='text/html')
        self.client.get(self.profile_url)
        response = self.client.get(self.export_url)
        self.assertEqual(response.status_code, 200)

    def test_percentage_aprovados(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        self.client.post(self.login_url, {'password': '#123456a', 'username': 'testemail@student.uc.pt'},
                         format='text/html')
        self.quiz1 = Quiz.objects.create(id=1, description='Matemática', question='Quanto é 3+6*8 ?', score=20,
                                         num_approvals=0, num_rejections=0, approval_state='Aprovado',
                                         creator=user, approver1=user,
                                         approver2=user, approver3=user,
                                         creation_date='2022-10-04 10:23:54+02', edited=False)
        response = self.client.get(self.profile_url)
        self.assertEqual(response.context['approved'], 100)

    def test_percentage_naoaprovados(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        user.save()
        self.client.post(self.login_url, {'password': '#123456a', 'username': 'testemail@student.uc.pt'},
                         format='text/html')
        self.quiz1 = Quiz.objects.create(id=1, description='Matemática', question='Quanto é 3+6*8 ?', score=20,
                                         num_approvals=0, num_rejections=0, approval_state='À espera de revisão',
                                         creator=user, approver1=user,
                                         approver2=user, approver3=user,
                                         creation_date='2022-10-04 10:23:54+02', edited=False)
        response = self.client.get(self.profile_url)
        self.assertEqual(response.context['approved'], 0)


class ExportXMLTests(TestCase):
    def setUp(self):
        self.export_url = reverse('quiz:Export Quizzes')
        self.login_url = reverse('login')

        exec(open('create_kahuc_groups.py').read())
        KahUCUser = get_user_model()
        self.user = KahUCUser.objects.create(
            is_superuser=False, username='teste@student.dei.uc.pt', first_name='teste1', last_name='teste1',
            email='teste@student.dei.uc.pt', is_staff=False, is_active=True)
        self.user.set_password("#123456a")
        creator_group = Group.objects.get(name='Creator')
        self.user.groups.add(creator_group)
        self.user.save()

        reviewer1 = KahUCUser.objects.create(
            is_superuser=False, username='teste1@student.dei.uc.pt', first_name='teste1', last_name='teste1',
            email='teste1@student.dei.uc.pt', is_staff=False, is_active=True)
        reviewer1.set_password("#123456a")

        reviewer2 = KahUCUser.objects.create(
            is_superuser=False, username='teste2@student.dei.uc.pt', first_name='teste2', last_name='teste2',
            email='teste2@student.dei.uc.pt', is_staff=False, is_active=True)
        reviewer2.set_password("#123456a")

        reviewer3 = KahUCUser.objects.create(
            is_superuser=False, username='teste3@student.dei.uc.pt', first_name='teste3', last_name='teste3',
            email='teste3@student.dei.uc.pt', is_staff=False, is_active=True)
        reviewer3.set_password("#123456a")

        reviewer_group = Group.objects.get(name='Reviewer')
        reviewer1.groups.add(reviewer_group)
        reviewer2.groups.add(reviewer_group)
        reviewer3.groups.add(reviewer_group)

        reviewer1.save()
        reviewer2.save()
        reviewer3.save()

        tag = Tag.objects.create(name="test_tag")
        tag.save()

        for i in range(101):
            quiz = Quiz.objects.create(id=i + 1, description='Quiz' + str(i), question='Pergunta do Quiz' + str(i),
                                       score=20, num_approvals=3,
                                       num_rejections=0, approval_state='Aprovado', creator=self.user,
                                       approver1=reviewer1,
                                       approver2=reviewer2, approver3=reviewer3,
                                       creation_date='2022-06-09 07:27:27+02', edited=False, tags=tag)
            quiz.save()

        return super().setUp()

    def test_export_0_quiz(self):
        self.client.post(self.login_url, {'username': 'teste@student.dei.uc.pt', 'password': '#123456a'},
                         format='text/html')
        response = self.client.post(self.export_url, {'questions': []})
        self.assertEqual(response.status_code, 200)

    def test_export_1_quiz(self):
        self.client.post(self.login_url, {'username': 'teste@student.dei.uc.pt', 'password': '#123456a'},
                         format='text/html')
        response = self.client.post(self.export_url, {'questions': ['1']})
        self.assertEqual(response.status_code, 200)

    def test_export_100_quiz(self):
        self.client.post(self.login_url, {'username': 'teste@student.dei.uc.pt', 'password': '#123456a'},
                         format='text/html')
        response = self.client.post(self.export_url, {'questions': [str(i + 1) for i in range(100)]})
        self.assertEqual(response.status_code, 200)

    def test_without_login(self):
        response = self.client.get(self.export_url)
        self.assertEqual(response.status_code, 302)
