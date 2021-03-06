"""
Django settings for Kinobase project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from urllib.parse import urlparse
import json
import ast
import dj_database_url
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    'static',
]

#
# heroku
#
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# deprecated STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#
# ENVIRONMENT SETUP
#
DEBUG = config('DEBUG', cast=bool)
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', '*').split(',')
LOGIN_REDIRECT_URL = 'movie_list'


#
# API and custom settings
#
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # One month

ANYMAIL = {
    "MAILGUN_API_KEY": config('MAILGUN_API_KEY'),
    "MAILGUN_SENDER_DOMAIN": config('MAILGUN_SENDER_DOMAIN'),  # your Mailgun domain, if needed
    "MAILGUN_API_URL": "https://api.eu.mailgun.net/v3"
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = 'admin@' + ANYMAIL['MAILGUN_SENDER_DOMAIN']
SERVER_EMAIL = 'admin@' + ANYMAIL['MAILGUN_SENDER_DOMAIN']

ACCOUNT_ACTIVATION_DAYS = 1  # One-day user activation window
REGISTRATION_AUTO_LOGIN = True
REGISTRATION_DEFAULT_FROM_EMAIL = 'admin@' + ANYMAIL['MAILGUN_SENDER_DOMAIN']

TMDB_API_KEY = config('TMDB_API_KEY_V3')
SECURE_BASE_URL = 'https://image.tmdb.org/t/p/'

STAR_RATINGS_RANGE = 10

# Application definition

AUTH_USER_MODEL = 'accounts.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'accounts',        # accounts must be before registration, else 'django-registration-redux' using it's own templates
    'registration',    # registration must be above 'django.contrib.auth'
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'star_ratings',
    'anymail',
    'movie',
]

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    INTERNAL_IPS = ('127.0.0.1', '192.168.1.149',)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware', # отсутствует в стандартном конфиге dj 3.0
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'kinobase.middleware.AjaxMessaging'
]
if DEBUG:
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

ROOT_URLCONF = 'kinobase.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
        ],
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

WSGI_APPLICATION = 'kinobase.wsgi.application'

#
# DATABASE
#

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME', ''),
        'USER': config('DATABASE_USER', ''),
        'PASSWORD': config('DATABASE_PASSWORD', ''),
        'HOST': config('DATABASE_HOST', ''),
        'PORT': '',
    }
}
# configure database for heroku
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

#
# CACHE
#
CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'LOCATION': config('MEMCACHEDCLOUD_SERVERS').split(','),
        'OPTIONS': {
            'username': config('MEMCACHEDCLOUD_USERNAME'),
            'password': config('MEMCACHEDCLOUD_PASSWORD')
        }
    }
}

if DEBUG:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
"""AUTH_PASSWORD_VALIDATORS = [
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
]"""


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = False


#
# Make django message type compatible to bootstrap alerts colors
#

from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
                message_constants.INFO: 'info',
                message_constants.SUCCESS: 'success',
                message_constants.WARNING: 'warning',
                message_constants.ERROR: 'danger'}

# list of predefined tags
PREDEFINED_TAGS = ['WATCHED', 'UNWATCHED', 'REJECTED', 'REJECTED', 'FAVOURITES']