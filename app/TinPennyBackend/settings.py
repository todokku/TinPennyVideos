"""
Django settings for TinPennyBackend project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', default=0))

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
AUTH_USER_MODEL = "accounts.User"

# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

EXTERNAL_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount', # Not required but have to keep - https://github.com/pennersr/django-allauth/issues/1975#issuecomment-384075169
    'storages',
    'corsheaders',
]

LOCAL_APPS = [
    'accounts.apps.AccountsConfig',
    'api.apps.ApiConfig',
    'media.apps.MediaConfig',
]

INSTALLED_APPS = DEFAULT_APPS + EXTERNAL_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'TinPennyBackend.cors.CorsMiddleware',
]

ROOT_URLCONF = 'TinPennyBackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'TinPennyBackend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('SQL_USER', 'user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', '5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Rest framework config
REST_FRAMEWORK = {
    # When you enable API versioning, the request.version attribute will contain a string
    # that corresponds to the version requested in the incoming client request.
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    # Permission settings
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoREST_FRAMEWORKModelPermissionsOrAnonReadOnly'
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
        # 'rest_framework.permissions.IsAuthenticated'
    ],
    # Authentication settings
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # Add this line for API explorer login
        'rest_framework.authentication.BasicAuthentication',
    ],

    # Pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

# JWT settings
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
        'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
        'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
        'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_AUTH_COOKIE': None,
}

REST_USE_JWT = True

SITE_ID = 1

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'api.serializers.LoginSerializer',
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.UserSerializer',
}

# django-allauth
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

# EMAIL CONFIG (We're using for sending register confirm/password change emails...)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Celery
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


# Media Related Settings
AWS_MEDIACONVERT_SQS_SUCCESS_URL = "https://sqs.us-east-2.amazonaws.com/045342251993/simple-video-sharing-platform"
AWS_MEDIACONVERT_SQS_FAILURE_URL = "https://sqs.us-east-2.amazonaws.com/045342251993/simple-video-sharing-platform_failure"
CLOUDFRONT_DNS_NAME = "d19q217zz3goo.cloudfront.net"
ACCEPTABLE_VIDEO_FILE_EXTENSIONS = ["mp4", "mpg", "mov", "mpeg"]

# S3 File Storage
FILE_STORAGE_FOR_ORIGIN_VIDEO = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'simple-video-sharing-platform-t4-sourcebucket-qbi8jojzvlrk3p'
AWS_STREAM_STORAGE_BUCKET_NAME = 'simple-video-sharing-platform-t-destinationbucket-qgx2mv4zsg9g'
AWS_S3_FILE_OVERWRITE = False

# Cors header
# Somehow its not working, had to depend on custom middleware to resolve CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False