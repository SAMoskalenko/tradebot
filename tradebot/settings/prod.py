import os

DEBUG = False

ALLOWED_HOSTS = ['*']

TELEGRAM_BOT_ID = os.environ['TELEGRAM_BOT_ID']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['POSTGRES_NAME'],
        'USER': os.environ['POSTGRES_NAME'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': '5432',
    }
}

