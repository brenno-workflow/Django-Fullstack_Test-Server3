"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Buscar as informações do arquivo .env
from dotenv import load_dotenv
import os

# Configurar url post db
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS").split(",")]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Adicionar os novos aplicativos
    'login',
    'account',
    'home',
    'curriculum',

    # Adicionar o cors
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
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

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        # Altera o motor de banco de dados para MySQL
        'ENGINE': os.getenv('DATABASE_ENGINE'), 
        # Nome do banco de dados  
        'NAME': os.getenv("DATABASE_NAME"), 
        # Usuário do banco de dados (padrão defaut - 'root')             
        'USER': os.getenv("DATABASE_USER"), 
        # Senha do banco de dados (se houver)                      
        'PASSWORD': os.getenv("DATABASE_PASSWORD"), 
        # Host do banco de dados (no caso, 'localhost')                       
        'HOST': os.getenv("DATABASE_HOST"),
        # Porta do banco de dados (opcional, padrão para MySQL é 3306)                   
        'PORT': os.getenv("DATABASE_PORT") 
    }
}

#ISSO
database_url = os.getenv("DATABASE_URL")
DATABASES['default'] = dj_database_url.parse(database_url)

# postgres://django_postgresql_evcx_user:Z39IoERquYBYndb3GEblSndv01sOakJq@dpg-com1o221hbls73998950-a/django_postgresql_evcx
# postgres://django_postgresql_evcx_user:Z39IoERquYBYndb3GEblSndv01sOakJq@dpg-com1o221hbls73998950-a.oregon-postgres.render.com/django_postgresql_evcx

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurar a configuração do REST Framework para API (GET, POST)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # Outros autenticadores, se houver
    ),
    # Outras configurações REST_FRAMEWORK, se houver
}
