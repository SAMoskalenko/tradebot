import environ

env = environ.Env()
environ.Env.read_env('.env')

DEBUG = True

TELEGRAM_BOT_ID = env('TELEGRAM_BOT_ID')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_NAME'),
        'USER': env('POSTGRES_NAME'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': '5432',
    }
}
