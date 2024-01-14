import os
from typing import List
import sys
import dj_database_url
from os import getenv, path
from pathlib import Path
from django.core.management.utils import get_random_secret_key
import dotenv



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = BASE_DIR / '.env.local'

if path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

DEVELOPMENT_MODE = getenv('DEVELOPMENT_MODE', 'False') == 'True'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
SECRET_KEY = getenv('DJANGO_SECRET_KEY', get_random_secret_key())


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = getenv('DJANGO_ALLOWED_HOSTS',
                       '127.0.0.1,localhost').split(',')

# Application definition
PREREQUISITE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'auditlog',
    'rest_framework',
    'celery',
    'djoser',
    'storages',
    'social_django',
]

PROJECT_APPS = [
    'myapp.apps.MyappConfig',
    'account.apps.AccountConfig',

]


INSTALLED_APPS = PREREQUISITE_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src_config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates', './base_templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
            ]
        },
    },
]

WSGI_APPLICATION = 'src_config.wsgi.application'

CORS_ALLOWED_ORIGINS = getenv(
    'CORS_ALLOWED_ORIGINS',
    'http://localhost:3000,http://127.0.0.1:3000'
).split(',')
CORS_ALLOW_CREDENTIALS = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # noqa : E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # noqa : E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # noqa : E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # noqa : E501
    },
]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGES = (
    ('pt-br', u'Português'),
    ('en', u'Inglês'),
)
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGE_CODE = 'pt-br'
USE_I18N = True

TIME_ZONE = 'America/Sao_Paulo'
USE_TZ = True

DECIMAL_SEPARATOR = ','
THOUSAND_SEPARATOR = '.'

# Authentication
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = 'account.UserAccount'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'account.authentication.CustomJWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'ACTIVATION_URL': 'activation/{uid}/{token}',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'TOKEN_MODEL': None,
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': getenv('REDIRECT_URLS').split(',')
}

AUTH_COOKIE = 'access'
AUTH_COOKIE_MAX_AGE = 60 * 60 * 24
AUTH_COOKIE_SECURE = getenv('AUTH_COOKIE_SECURE', 'True') == 'True'
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = '/'
AUTH_COOKIE_SAMESITE = 'None'


# Email settings

EMAIL_BACKEND = 'django_ses.SESBackend'
DEFAULT_FROM_EMAIL = getenv('AWS_SES_FROM_EMAIL')

AWS_SES_ACCESS_KEY_ID = getenv('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = getenv('AWS_SES_SECRET_ACCESS_KEY')
AWS_SES_REGION_NAME = getenv('AWS_SES_REGION_NAME')
AWS_SES_REGION_ENDPOINT = f'email.{AWS_SES_REGION_NAME}.amazonaws.com'
AWS_SES_FROM_EMAIL = getenv('AWS_SES_FROM_EMAIL')
USE_SES_V2 = True

DOMAIN = getenv('DOMAIN')
SITE_NAME = 'Full Auth'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
if DEVELOPMENT_MODE is True:
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / 'static'
    MEDIA_URL = 'media/'
    MEDIA_ROOT = BASE_DIR / 'media'
else:
    AWS_S3_ACCESS_KEY_ID = getenv('AWS_S3_ACCESS_KEY_ID')
    AWS_S3_SECRET_ACCESS_KEY = getenv('AWS_S3_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = getenv('AWS_S3_REGION_NAME')
    AWS_S3_ENDPOINT_URL = f'https://{AWS_S3_REGION_NAME}.digitaloceanspaces.com'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400'
    }
    AWS_DEFAULT_ACL = 'public-read'
    AWS_LOCATION = 'static'
    AWS_MEDIA_LOCATION = 'media'
    AWS_S3_CUSTOM_DOMAIN = getenv('AWS_S3_CUSTOM_DOMAIN')
    STORAGES = {
        'default': {'BACKEND': 'custom_storages.CustomS3Boto3Storage'},
        'staticfiles': {'BACKEND': 'storages.backends.s3boto3.S3StaticStorage'}
    }

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'




LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'celery': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

try:
    from .local_settings import * # noqa : F403,F401
except ImportError:
    print('No Local Settings Found')
