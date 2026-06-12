"""
Django settings for projeto_despesas project.
"""
import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Em produção no Heroku/Render, configure uma variável de ambiente 'DJANGO_SECRET_KEY'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-(z^%l1uqtjkr8xdx)1ajt)$+n#zv3zy*6jr@o+ikb4@8$lz)0n')

# Segurança: DEBUG fica False em produção automaticamente se definirmos a variável
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Permite conexões locais e do subdomínio do Render
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.onrender.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'despesas', 
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Essencial para o CSS funcionar na nuvem
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projeto_despesas.urls'

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

WSGI_APPLICATION = 'projeto_despesas.wsgi.application'

# =====================================================================
# CONFIGURAÇÃO DE BANCO DE DADOS (Híbrida: Local vs Nuvem)
# =====================================================================
DATABASE_URL = os.environ.get('JAWSDB_URL') or os.environ.get('CLEARDB_DATABASE_URL') or os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # Se estiver no Render, configura o banco da nuvem dinamicamente
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600)
    }
else:
    # Se estiver no seu PC, mantém o seu MySQL local padrão intacto
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'despesas_db',
            'USER': 'root',
            'PASSWORD': '68425500',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }

# Localização e Idioma ajustados
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# =====================================================================
# CONFIGURAÇÃO DE ARQUIVOS ESTÁTICOS (WhiteNoise - Padrão Django 6+)
# =====================================================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# =====================================================================
# CONFIGURAÇÃO DE CACHE (Performance da API)
# =====================================================================
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'api-despesas-cache',
    }
}

# =====================================================================
# LOGGING (Ajustado para o Render - Saída via Consola/Stream)
# =====================================================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# =====================================================================
# CONFIGURAÇÕES DO FLUXO DE AUTENTICAÇÃO
# =====================================================================
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'listar'
LOGOUT_REDIRECT_URL = 'login'