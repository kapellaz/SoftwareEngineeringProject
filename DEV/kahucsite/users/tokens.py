import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """
    Gerador de token para reset de password e ativacao de conta
    """

    def _make_has_value(self, user, timestamp):
        """
        Utilizado para construir um URL onde o utilizador acede para confirmar conta
        :param user: utilizador
        :param timestamp: tempo de ocorrencia
        :return: token para URL
        """
        return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)


account_activation_token = AccountActivationTokenGenerator()
