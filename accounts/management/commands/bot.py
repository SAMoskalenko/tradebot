from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User

from telegram import Update
from telegram.ext import (CallbackContext,
                          CommandHandler,
                          Updater)
# from telegram.ext import CommandHandler
# from telegram.ext import Filters
# from telegram.ext import MessageHandler
# from telegram.ext import Updater

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
def do_depth(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    check = checking(chat_id)
    if check:
        symbol = update.message['text'].split(' ')[1]
        u = BinanceAPI()
        t = u.get_depth(symbol).json()
        try:
            u = t['code']
            update.message.reply_text(
                text=f'Неверный символ Binance',
            )
        except:
            update.message.reply_text(
                text=f'Данные стакана {t}',
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
        t = u.account().json()
        try:
            u = t['code']
            update.message.reply_text(
                text=f'Заполните данные вашего аккаунта Binance',
            )
        except:
            update.message.reply_text(
                text=f'Данные вашего аккаунта {t}',
            )
    else:
        update.message.reply_text(
            text=f'Заполните account ваш chat_id: {chat_id}',
        )


@log_errors
def do_newOrder(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    check = checking(chat_id)
    if check:
        secret = UserAccount.objects.get(chat_id=chat_id).binance_secret
        key = UserAccount.objects.get(chat_id=chat_id).binance_key
        u = BinanceAPI(secret, key)
        t = u.newOrder().json()
        try:
            u = t['code']
            update.message.reply_text(
                text=f'Заполните данные вашего аккаунта Binance',
            )
        except:
            update.message.reply_text(
                text=f'Данные вашего аккаунта {t}',
            )
    else:
        update.message.reply_text(
            text=f'Заполните account ваш chat_id: {chat_id}',
        )


@log_errors
def do_queryOrder(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    check = checking(chat_id)
    if check:
        secret = UserAccount.objects.get(chat_id=chat_id).binance_secret
        key = UserAccount.objects.get(chat_id=chat_id).binance_key
        symbol = update.message['text'].split(' ')[1]
        order_id = update.message['text'].split(' ')[2]
        u = BinanceAPI(secret, key)
        t = u.queryOrder(symbol, order_id).json()
        try:
            u = t['code']
            update.message.reply_text(
                text=f'Заполните данные вашего аккаунта Binance',
            )
        except:
            update.message.reply_text(
                text=f'Статус вашего ордера с номером {order_id} ',
            )
    else:
        update.message.reply_text(
            text=f'Заполните account ваш chat_id: {chat_id}',
        )


@log_errors
def do_deleteOrder(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    check = checking(chat_id)
    if check:
        secret = UserAccount.objects.get(chat_id=chat_id).binance_secret
        key = UserAccount.objects.get(chat_id=chat_id).binance_key
        symbol = update.message['text'].split(' ')[1]
        order_id = update.message['text'].split(' ')[2]
        u = BinanceAPI(secret, key)
        t = u.deleteOrder(symbol, order_id).json()
        try:
            u = t['code']
            update.message.reply_text(
                text=f'Заполните данные вашего аккаунта Binance',
            )
        except:
            update.message.reply_text(
                text=f'Ордер с номером {order_id} удален',
            )
    else:
        update.message.reply_text(
            text=f'Заполните account ваш chat_id: {chat_id}',
        )


@log_errors
def do_openOrders(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    check = checking(chat_id)
    if check:
        secret = UserAccount.objects.get(chat_id=chat_id).binance_secret
        key = UserAccount.objects.get(chat_id=chat_id).binance_key
        symbol = update.message['text'].split(' ')[1]
        u = BinanceAPI(secret, key)
        t = u.openOrders(symbol).json()
        try:
            u = t['code']
            update.message.reply_text(
                text=f'Заполните данные вашего аккаунта Binance',
            )
        except:
            update.message.reply_text(
                text=f'Все открытые заявки с {symbol} {t}',
            )
    else:
        update.message.reply_text(
            text=f'Заполните account ваш chat_id: {chat_id}',
        )


@log_errors
def do_allOrders(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    check = checking(chat_id)
    if check:
        secret = UserAccount.objects.get(chat_id=chat_id).binance_secret
        key = UserAccount.objects.get(chat_id=chat_id).binance_key
        symbol = update.message['text'].split(' ')[1]
        u = BinanceAPI(secret, key)
        t = u.allOrders(symbol).json()
        try:
            u = t['code']
            update.message.reply_text(
                text=f'Заполните данные вашего аккаунта Binance',
            )
        except:
            update.message.reply_text(
                text=f'Все заявки с {symbol} {t}',
            )
    else:
        update.message.reply_text(
            text=f'Заполните account ваш chat_id: {chat_id}',
        )


@log_errors
def do_myTrades(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    check = checking(chat_id)
    if check:
        secret = UserAccount.objects.get(chat_id=chat_id).binance_secret
        key = UserAccount.objects.get(chat_id=chat_id).binance_key
        symbol = update.message['text'].split(' ')[1]
        u = BinanceAPI(secret, key)
        t = u.myTrades(symbol).json()
        try:
            u = t['code']
            update.message.reply_text(
                text=f'Заполните данные вашего аккаунта Binance',
            )
        except:
            update.message.reply_text(
                text=f'Ваши сделки {t}',
            )
    else:
        update.message.reply_text(
            text=f'Заполните account ваш chat_id: {chat_id}',
        )


@log_errors
def do_depositHistory(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    check = checking(chat_id)
    if check:
        secret = UserAccount.objects.get(chat_id=chat_id).binance_secret
        key = UserAccount.objects.get(chat_id=chat_id).binance_key
        u = BinanceAPI(secret, key)
        t = u.depositHistory().json()
        try:
            u = t['code']
            update.message.reply_text(
                text=f'Заполните данные вашего аккаунта Binance',
            )
        except:
            update.message.reply_text(
                text=f'Данные о вводе средств на ваш аккаунта {t}',
            )
    else:
        update.message.reply_text(
            text=f'Заполните account ваш chat_id: {chat_id}',
        )


@log_errors
def do_withdrawHistory(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    check = checking(chat_id)
    if check:
        secret = UserAccount.objects.get(chat_id=chat_id).binance_secret
        key = UserAccount.objects.get(chat_id=chat_id).binance_key
        u = BinanceAPI(secret, key)
        t = u.withdrawHistory().json()
        try:
            u = t['code']
            update.message.reply_text(
                text=f'Заполните данные вашего аккаунта Binance',
            )
        except:
            update.message.reply_text(
                text=f'Данные о выводе средств с вашего аккаунта {t}',
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
        updater.dispatcher.add_handler(CommandHandler('depth', do_depth))
        updater.dispatcher.add_handler(CommandHandler('account', do_account))
        updater.dispatcher.add_handler(CommandHandler('newOrder', do_newOrder))
        updater.dispatcher.add_handler(CommandHandler('deleteOrder', do_deleteOrder))
        updater.dispatcher.add_handler(CommandHandler('queryOrder', do_queryOrder))
        updater.dispatcher.add_handler(CommandHandler('allOrders', do_allOrders))
        updater.dispatcher.add_handler(CommandHandler('openOrders', do_openOrders))
        updater.dispatcher.add_handler(CommandHandler('myTrades', do_myTrades))
        updater.dispatcher.add_handler(CommandHandler('withdrawHistory', do_withdrawHistory))
        updater.dispatcher.add_handler(CommandHandler('depositHistory', do_depositHistory))

        updater.start_polling()
        updater.idle()
