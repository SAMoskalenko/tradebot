# Binance tradebot

# Устанавливаем зависимости

pip install -r requirements.txt 

pip install pipenv

pipenv install --system

cd tradebot-front

npm install

# Запускаем проект

В корневом каталоге "tradebot" запускаем 

Django командой:

python manage.py runserver

Телеграм бот командой:

python manage.py bot

Запускаем Vue в каталоге "tradebot-front", для этого:

Меняем каталог командой:

cd tradebot-front

Запускаем Vue командой:

npm run dev

# Работа с проектом

Имя бота @GB_test_tradebot (ВНИМАНИЕ для работы на территории РФ необходим VPN)

Регистрисруемся через Vue заносим данные бота и Binance

# Доступные команды

/time - возвращаяет время сервера

/account - возвращает данные аккаунта Binance
