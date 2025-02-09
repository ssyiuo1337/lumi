from datetime import timedelta
import dj_database_url
from pathlib import Path
import os


from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0x4AAAAAAA5_BiyXQG1tFtQrtlWq1KcTTHA'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['backend', 'localhost', '127.0.0.1', 'euw.devtunnels.ms', 'drainwalk.tech', 'frontend', 'xmcn2wj6-5173.euw.devtunnels.ms', 'xmcn2wj6-5173.euw.devtunnels.ms', 'xmcn2wj6-8000.euw.devtunnels.ms', 'lumi-yue2.onrender.com', 'lumi-24al.onrender.com', 'projectcube.tech']

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:5173',
    'https://projectcube.tech',
    'https://lumi-24al.onrender.com',
    'https://lumi-yue2.onrender.com',
    'https://xmcn2wj6-5173.euw.devtunnels.ms',
    'https://xmcn2wj6-8000.euw.devtunnels.ms',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:5173',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8000',
    'https://xmcn2wj6-5173.euw.devtunnels.ms',
    'https://drainwalk.tech'
]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'rest_framework',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'authorization',
    'file_system',
    'user_statistics',
    'subscription',
    'payment'

]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://lumi-24al.onrender.com",
    "https://projectcube.tech",
    "https://xmcn2wj6-5173.euw.devtunnels.ms",
    "https://xmcn2wj6-8000.euw.devtunnels.ms",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "https://lumi-yue2.onrender.com"
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8000",
    "https://xmcn2wj6-5173.euw.devtunnels.ms",
    "https://drainwalk.tech"
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'authorization.backends.RoleBasedBackend'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://lumi-24al.onrender.com",
    "https://xmcn2wj6-5173.euw.devtunnels.ms",
    "https://xmcn2wj6-8000.euw.devtunnels.ms",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "https://projectcube.tech",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8000",
    "https://lumi-yue2.onrender.com",
    "https://xmcn2wj6-5173.euw.devtunnels.ms",
    "https://drainwalk.tech"
]

ROOT_URLCONF = 'dw_backend.urls'

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

WSGI_APPLICATION = 'dw_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
     'ENGINE': 'django.db.backends.postgresql',
     'default': dj_database_url.config(
         default=os.environ.get('postgresql://yiuo:DTXc69m0H5TqwXIA3cTgnayMdoKpyzt8@dpg-cujq8kqj1k6c73d115v0-a/world_gajz')
     )
 }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'authorization.DwUser'

SECRET_KEY = '0x4AAAAAAA5_BiyXQG1tFtQrtlWq1KcTTHA'

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),

    "SIGNING_KEY": settings.SECRET_KEY
}

import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        # Добавляем логгер для вашего приложения
        'authorization': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CLOUDFLARE_TURNSTILE_SECRET_KEY = '0x4AAAAAAA5_BiyXQG1tFtQrtlWq1KcTTHA'
