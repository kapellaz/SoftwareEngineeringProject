import re

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordResetForm
from django.core.validators import FileExtensionValidator

from . import models


class SetNewPassword(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

    def clean_new_password2(self):
        """
        Função para validar as palavras-chave inseridas pelo utilizador
        :return: passwords validadas
        """
        password1 = self.cleaned_data.get('new_password1')
        if not password1:
            raise forms.ValidationError('É necessário inserir uma palavra-passe!')
        password2 = self.cleaned_data.get('new_password2')
        if not password2:
            raise forms.ValidationError('É necessário voltar a inserir a sua palavra-passe!')

        if password1 != password2:
            raise forms.ValidationError('Palavras-passe não são iguais!')

        password = password1

        if len(password) < 8:
            raise forms.ValidationError('Palavra-passe tem de ter pelo menos 8 carateres!')

        if not re.search('[A-Za-z]', password):
            raise forms.ValidationError('Palavra-passe tem de ter pelo menos 1 letra!')
        if not re.search('[0-9]', password):
            raise forms.ValidationError('Palavra-passe tem de ter pelo menos 1 número!')
        if not re.search("[\\\~`! @#$%^&*()_\-+={\[}\]|:;\"'<,>.?/]", password):
            raise forms.ValidationError('Palavra-passe tem de ter pelo menos 1 carater especial!')

        return password


class PasswordReset(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)


class RegisterUser(UserCreationForm):
    """
    Formulário de registo baseado no UserCreationForm do Django
    """
    first_name = forms.CharField(label='First Name', max_length=20, min_length=2)
    last_name = forms.CharField(label='Last Name', max_length=20, min_length=2)

    class Meta:
        """
        Classe que define o modelo de user a utilizar e os campos a preencher no formulário de registo
        """
        model = models.KahUCUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')

    def clean_username(self):
        """
        Função para validar o email inserido pelo utilizador
        :return: email validado
        """
        email = self.cleaned_data.get('username')
        if not email:
            raise forms.ValidationError('É necessário inserir um email institucional!')

        if ('@' not in email or
                ('@' in email and email[email.index('@'):] not in ["@student.dei.uc.pt", "@dei.uc.pt",
                                                                   "@student.uc.pt"])):
            raise forms.ValidationError('Email inválido')

        try:
            user_with_username = models.KahUCUser.objects.get(username=email)
        except:
            user_with_username = None

        if user_with_username:
            raise forms.ValidationError('Já existe uma conta com este endereço de email!')

        return email

    def clean_password2(self):
        """
        Função para validar as palavras-chave inseridas pelo utilizador
        :return: passwords validadas
        """
        password1 = self.cleaned_data.get('password1')
        if not password1:
            raise forms.ValidationError('É necessário inserir uma palavra-passe!')
        password2 = self.cleaned_data.get('password2')
        if not password2:
            raise forms.ValidationError('É necessário voltar a inserir a sua palavra-passe!')

        if password1 != password2:
            raise forms.ValidationError('Palavras-passe não são iguais!')

        password = password1

        if len(password) < 8:
            raise forms.ValidationError('Palavra-passe tem de ter pelo menos 8 carateres!')

        if not re.search('[A-Za-z]', password):
            raise forms.ValidationError('Palavra-passe tem de ter pelo menos 1 letra!')
        if not re.search('[0-9]', password):
            raise forms.ValidationError('Palavra-passe tem de ter pelo menos 1 número!')
        if not re.search("[\\\~`! @#$%^&*()_\-+={\[}\]|:;\"'<,>.?/]", password):
            raise forms.ValidationError('Palavra-passe tem de ter pelo menos 1 carater especial!')

        return password

    def clean_first_name(self):
        """
        Função para validar o primeiro nome inserido pelo utilizador
        :return: primeiro nome validado
        """
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError('Por favor indique o seu primeiro nome!')
        return first_name

    def clean_last_name(self):
        """
        Função para validar o último nome inserido pelo utilizador
        :return: último nome validado
        """
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError('Por favor indique o seu último nome!')
        return last_name


class ImportXMLForm(forms.Form):
    file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['xml'])])
