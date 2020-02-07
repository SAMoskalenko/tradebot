import environ
from .base import *

env = environ.Env()
environ.Env.read_env('.env')

DEBUG = True

TELEGRAM_BOT_ID = env('TELEGRAM_BOT_ID')
