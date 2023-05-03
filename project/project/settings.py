"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv  # для защиты личных данных

load_dotenv()  # получить доступ к значениям переменных среды, используя os.environ:

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_4ve7b%*tuz8fpio2j2%c=d)awx@5jhu294+o^_mt5z-vh9+#_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',  # добавляет пользователей
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',  # добавляет сообщения
    'django.contrib.staticfiles',

    'new_portal',
    'news',
    'django_filters',
    'django.contrib.sites',  # # добавляет настройки сайта

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',  # поддержка входа с помощью Yandex
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # `allauth` обязательно нужен этот процессор
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'
# 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / 'new_portal' / 'static',
]

LOGIN_REDIRECT_URL = '/news'  # После входа, нас перебросит на список всех новостей

# Этого раздела может не быть, добавьте его в указанном виде.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # встроенный бэкенд Django реализующий аутентификацию по username;
    'allauth.account.auth_backends.AuthenticationBackend',  # бэкенд аутентификации, предоставленный пакетом allauth
]

ACCOUNT_EMAIL_REQUIRED = True            # поле email является обязательным
ACCOUNT_UNIQUE_EMAIL = True              # поле email является уникальным
ACCOUNT_USERNAME_REQUIRED = False        # username необязательный
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # аутентификация будет происходить посредством электронной почты
ACCOUNT_EMAIL_VERIFICATION = 'none'      # верификация почты отсутствует
ACCOUNT_FORMS = {'signup': 'accounts.forms.CustomSignupForm'}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # для отправки писем на реальные почтовые адреса
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Для тестирования, печать писем в консоль.

EMAIL_HOST = 'smtp.yandex.ru'                                # хост почтового сервера
EMAIL_PORT = 465                                             # порт, на который почтовый сервер принимает письма
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')          # логин пользователя почтового сервера
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')  # пароль пользователя почтового сервера
EMAIL_USE_TLS = False                                    # необходимость использования TLS (зависит от почтового сервера
EMAIL_USE_SSL = True                                     # необходимость использования SSL (зависит от почтового сервера

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')  # почтовый адрес отправителя по умолчанию

SERVER_EMAIL = os.environ.get('SERVER_EMAIL')

# при новой регистрации, данному списку менеджеров будет приходить оповещение
MANAGERS = (
    ('manager', 'ServisVLG4@yandex.ru'),
)

# при новой регистрации, данному списку администраторов будет приходить оповещение
ADMINS = (
    ('administrator', 'servisvlg4@rambler.ru'),
)