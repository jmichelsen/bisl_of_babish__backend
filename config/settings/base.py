"""
Django settings for bisl project.

Generated by 'django-admin startproject' using Django 2.0b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from unipath import Path

from common.utils import get_env_variable, set_env_from_secrets

# Build paths inside the project like this: BASE_DIR.child('dirname')
BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = 'aiz&fx%x9)bi_g$hl*c!*asiall(w@-34tm%&=urx=_%k447l_'
DEBUG = True
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # local apps
    'common',
    'comments',
    'recipes',

    # third party
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
# LOGIN_REDIRECT_URL = 'home:index' or whatever
PASSWORD_RESET_TIMEOUT_DAYS = 1

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_HOST = get_env_variable('DJANGO_STATIC_HOST', default='')
STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_DIR = BASE_DIR.child('static')
STATICFILES_DIRS = [STATIC_DIR, ]
STATIC_URL = STATIC_HOST + '/static/'


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_AUTO_CREATE_BUCKET = True
AWS_S3_FILE_OVERWRITE = False
AWS_LOCATION = 'mms'


# Python logger setup
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'verbose': {
            'format': 'bisl[%(process)d]: %(levelname)s %(name)s[%(module)s] %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'verbose',
            'address': '/dev/log',
            'facility': 'local2',
        },
        'celery': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'urllib3': {
            'handlers': ['console', 'syslog'],
            'propagate': True,
            'level': 'ERROR',
        },
        'celery': {
            'handlers': ['celery', 'syslog'],
            'propagate': True,
            'level': 'DEBUG',
        },
        '': {
            'handlers': ['console', 'syslog'],
            'level': 'DEBUG',
        },
    },
}


#############
# API Configs
#############
set_env_from_secrets()

