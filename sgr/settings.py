
"""
Django settings for sgr project.

Proyecto: SGR_BackEnd
Evaluación Sumativa N°3 - Programación Back-End
Django 6.1.1
"""

from pathlib import Path
import os
from dotenv import load_dotenv


# ==========================================
# RUTAS DEL PROYECTO
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')


# ==========================================
# SEGURIDAD
# ==========================================

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '')

DEBUG = os.getenv('DJANGO_DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]


# ==========================================
# APLICACIONES INSTALADAS
# ==========================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Aplicaciones del SGR
    'app_funcionarios',
    'app_actividades',
    'app_usuarios',
    'app_delegaciones',
    'app_cargos',
    'app_seguimientos',
]


# ==========================================
# MIDDLEWARE
# ==========================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==========================================
# URLS Y TEMPLATES
# ==========================================

ROOT_URLCONF = 'sgr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'templates',
        ],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sgr.wsgi.application'


# ==========================================
# BASE DE DATOS - MYSQL
# ==========================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',

        'NAME': os.getenv('DB_NAME'),

        'USER': os.getenv('DB_USER'),

        'PASSWORD': os.getenv('DB_PASSWORD'),

        'HOST': os.getenv('DB_HOST'),

        'PORT': os.getenv('DB_PORT'),

        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# ==========================================
# VALIDACIÓN DE CONTRASEÑAS
# ==========================================

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


# ==========================================
# IDIOMA Y ZONA HORARIA
# ==========================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# ==========================================
# ARCHIVOS ESTÁTICOS
# ==========================================

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# ==========================================
# CORREO ELECTRÓNICO - GMAIL SMTP
# ==========================================

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.smtp.EmailBackend',

        'OPTIONS': {
            'host': os.getenv('SMTP_HOST', 'smtp.gmail.com'),

            'port': int(os.getenv('SMTP_PORT', '587')),

            'username': os.getenv('SMTP_USER', ''),

            'password': os.getenv(
                'SMTP_APP_PASSWORD', ''
            ).replace(' ', ''),

            'use_tls': os.getenv(
                'SMTP_USE_TLS', 'True'
            ).lower() == 'true',

            'timeout': 15,
        },
    },
}


# Remitente de los correos del SGR
DEFAULT_FROM_EMAIL = os.getenv('SMTP_USER', '')
