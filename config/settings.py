"""
Django settings for reservation_api project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os

from django.core.exceptions import ImproperlyConfigured

import dj_database_url
from unipath import Path


# Helper functions

def env(name, default=None):
    return os.environ.get(name, default)

def require_env(name):
    value = env(name)
    if not value:
        raise ImproperlyConfigured('Missing {} env variable'.format(name))
    return value

true_values = ['1', 'true', 'y', 'yes', 1, True]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = require_env('DJANGO_DEBUG').lower() in true_values

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', 'DEBUG_SECRET_KEY')
if SECRET_KEY == 'DEBUG_SECRET_KEY' and DEBUG is False:
    raise ImproperlyConfigured('Missing SECRET_KEY env variable. You can ' +
            'generate one with `./manage.py generate_secret_key`.')

if DEBUG is False:
    ALLOWED_HOSTS = ['reservations.coredump.ch']
else:
    ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    'reservations',
)

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'config.urls'

PROJECT_ROOT = Path(__file__).ancestor(2)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database

DATABASES = {
    'default': dj_database_url.config(),
}


# REST Framework

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'PAGE_SIZE': 20
}


# CORS

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'

# Session

# We disable the session cookie httponly flag, so that the session can be
# terminated from JavaScript by removing this cookie. This increases the CSS
# risk a bit, but this is not a critical API :)
SESSION_COOKIE_HTTPONLY = False


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = PROJECT_ROOT.child('static')
MEDIA_ROOT = PROJECT_ROOT.child('media')
