# flake8: noqa
import logging

from config.settings.base import *

logging.disable(logging.CRITICAL)

SECRET_KEY = 'not so secret, only used for tests'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': get_env_variable('PSQL_HOST'),
        'NAME': get_env_variable('PSQL_NAME'),
        'USER': get_env_variable('PSQL_USERNAME'),
        'PASSWORD': get_env_variable('PSQL_USERNAME'),
    }
}
