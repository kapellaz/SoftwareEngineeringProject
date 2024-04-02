"""
Definições Django para o projeto kahucsite.

Docs:
https://docs.djangoproject.com/en/4.1/topics/settings/
https://docs.djangoproject.com/en/4.1/ref/settings/

Checklist de segurança para produção:
https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: chave deve ser secreta!
# SECRET_KEY = os.environ['CURRENT_SECRET_KEY']
SECRET_KEY = 'django-insecure-^0o+whz54ozuzuzu!u!!!uughfyf%17dhdhyrghbhjnjghgbui'

# SECURITY WARNING: debug deve estar desligado em produção!
DEBUG = True

# Com debug desligado, hosts permitidos devem ser listados
# para produção: listar hosts permitidos
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'create_test',
    'hall_of_fame',
    'historic_quiz',
    'quiz',
    'review_quiz',
    'solve_test',
    'test_results',
    'users',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Modelo de utilizador a usar
AUTH_USER_MODEL = 'users.KahUCUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kahucsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kahucsite.dev_wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_FROM = 'kahuc.es2022@gmail.com'  # por completar meter email do site
EMAIL_HOST_USER = 'kahuc.es2022@gmail.com'  # same
EMAIL_HOST_PASSWORD = 'uffiopchonzscywg'  # same

PASSWORD_RESET_TIMEOUT = 15 * 60

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'temp_db_name',
        'USER': 'temp_user_name',
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

# Estes validators não coincidem com o que é necessário, por isso foram reescritos no users/forms.py (by Grupo 1)
"""
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
"""

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-PT'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = BASE_DIR / 'static_root/'

STATIC_URL = 'static/'

STATICFILES_DIRS = (
    BASE_DIR / 'static/',
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# É necessário isto para o django registar os models e apps criadas
# django.setup()

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# tempo que uma sessao de login dura, se clicar em "lembrar-me"
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30

# Altera session cookies com cada request, simplifica alteração da sessão
SESSION_SAVE_EVERY_REQUEST = True

# Link da página de login
LOGIN_URL = '/users/login/'
