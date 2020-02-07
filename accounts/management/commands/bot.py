from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

from django.conf import settings

from accounts.models import UserAccount

from binance import BinanceAPI


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e

    return inner


@log_errors
def checking(chat_id, check=False):
    try:
        UserAccount.objects.get(chat_id=chat_id)
        check = True
    except:
        pass
    return check


@log_errors
def do_time(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    check = checking(chat_id)
    if check:
        u = BinanceAPI()
        t = u.get_time().json()
        update.message.reply_text(
            text=f'Текущее время {t}',
        )
    else:
        update.message.reply_text(
            text=f'Заполните account ваш chat_id: {chat_id}',
        )


@log_errors
def do_account(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    check = checking(chat_id)
    if check:
        secret = UserAccount.objects.get(chat_id=chat_id).binance_secret
        key = UserAccount.objects.get(chat_id=chat_id).binance_key
        u = BinanceAPI(secret, key)
        t = u.get_account().json()
        update.message.reply_text(
            text=f'Данные вашего аккаунта {t}',
        )
    else:
        update.message.reply_text(
            text=f'Заполните account ваш chat_id: {chat_id}',
        )


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater(
            token=settings.TELEGRAM_BOT_ID,
            use_context=True,
        )

        updater.dispatcher.add_handler(CommandHandler('time', do_time))
        updater.dispatcher.add_handler(CommandHandler('account', do_account))

        updater.start_polling()
        updater.idle()
