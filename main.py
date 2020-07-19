import telebot
import random

from parse import auto_sales, shoes_sales, computer_sales, tour_sales, sport_sales, food_sales, clothes_sales, \
    games_sales, games_promo, shoes_promo, clothes_promo, auto_promo, tour_promo, sport_promo, food_promo, \
    computer_promo, cool_sales

bot = telebot.TeleBot(token)
keyboard = telebot.types.ReplyKeyboardMarkup()
key = telebot.types.ReplyKeyboardMarkup()
keys = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Скидончики', 'Промокодики')
keyboard.row('Лучшие предложения')
keys.row('Автотовары 🚗', 'Одежда 👕', 'Игры 🎮')
keys.row('Обувь 👠', 'Спорт и отдых ⚽', 'Еда 🍔')
keys.row('Компьютеры и электроника 💻', 'Туры и путешествия 🛫')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,
                     'Бот Mr Saler поможет тебе получить полезные скидончики и промокодики в нужной категории'
                     'также бот будет держать тебя в курсе лучших предложений дня!')
    bot.send_message(message.chat.id, 'Используй эти команды для общения с ботом:\n'
                                      '/start - начать общение\n'
                                      '/help - получить информацию про бота\n')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет, {}! Вижу ты устал от жутких цен,но не отчаивайся,'
                     'ведь я был создан с одной лишь целью - помочь тебе найти подходящий скидон'
                     .format(message.from_user.first_name), reply_markup=keyboard)
    bot.send_message(message.chat.id, 'Используй эти команды для общения с ботом:\n'
                                      '/start - начать общение\n'
                                      '/help - получить информацию про бота\n')
    bot.send_message(message.chat.id, 'Если нужны годные предожения, то "лучшие предложения" тебе помогут!')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Скидончики':
        bot.send_message(message.chat.id, 'Какую категорию хочешь посмотреть?', reply_markup=keys)
        bot.register_next_step_handler(message, start_sale)
    elif message.text == 'Промокодики':
        bot.send_message(message.chat.id, 'Отлично! Какую категорию хочешь посмотреть?', reply_markup=keys)
        bot.register_next_step_handler(message, get_promo)
    elif message.text == 'Лучшие предложения':
        bot.send_message(message.chat.id, 'Предложения на  сегодня: ')
        send_sticker(message)
    else:
        bot.send_message(message.chat.id, 'Извини, {}, но я тебя не понимаю('.format(message.from_user.first_name))


def get_promo(message):
    if message.text == 'Автотовары 🚗':
        bot.send_message(message.chat.id, 'Лови!')
        promo_auto(message)
    elif message.text == 'Одежда 👕':
        bot.send_message(message.chat.id, 'Круто!')
        promo_clothes(message)
    elif message.text == 'Игры 🎮':
        bot.send_message(message.chat.id, 'Начнем!')
        promo_games(message)
    elif message.text == 'Обувь 👠':
        bot.send_message(message.chat.id, 'Начнем!')
        promo_shoes(message)
    elif message.text == 'Компьютеры и электроника 💻':
        bot.send_message(message.chat.id, 'Начнем!')
        promo_computers(message)
    elif message.text == 'Туры и путешествия 🛫':
        bot.send_message(message.chat.id, 'Начнем!')
        promo_tours(message)
    elif message.text == 'Спорт и отдых ⚽':
        bot.send_message(message.chat.id, 'Начнем!')
        promo_sports(message)
    elif message.text == 'Еда 🍔':
        bot.send_message(message.chat.id, 'Начнем!')
        promo_food(message)
    else:
        bot.send_message(message.chat.id, 'Извини, {}, но я тебя не понимаю('.format(message.from_user.first_name))


def start_sale(message):
    if message.text == 'Автотовары 🚗':
        bot.send_message(message.chat.id, 'Лови!')
        start_auto(message)
    elif message.text == 'Одежда 👕':
        bot.send_message(message.chat.id, 'Круто!')
        start_clothes(message)
    elif message.text == 'Игры 🎮':
        bot.send_message(message.chat.id, 'Начнем!')
        start_games(message)
    elif message.text == 'Обувь 👠':
        bot.send_message(message.chat.id, 'Начнем!')
        start_shoes(message)
    elif message.text == 'Компьютеры и электроника 💻':
        bot.send_message(message.chat.id, 'Начнем!')
        start_computers(message)
    elif message.text == 'Туры и путешествия 🛫':
        bot.send_message(message.chat.id, 'Начнем!')
        start_tours(message)
    elif message.text == 'Спорт и отдых ⚽':
        bot.send_message(message.chat.id, 'Начнем!')
        start_sports(message)
    elif message.text == 'Еда 🍔':
        bot.send_message(message.chat.id, 'Начнем!')
        start_food(message)
    else:
        bot.send_message(message.chat.id, 'Извини, {}, но я тебя не понимаю('.format(message.from_user.first_name))


def start_auto(message):
    bot.send_message(message.chat.id, 'Кайфовые скидки для автотоваров:', reply_markup=keyboard)
    for key, value in auto_sales().items():
        bot.send_photo(message.chat.id, value, caption=key)


def start_clothes(message):
    bot.send_message(message.chat.id, 'Кайфовые скидки на шмот:', reply_markup=keyboard)
    for key, value in clothes_sales().items():
        bot.send_photo(message.chat.id, value, caption=key)


def start_games(message):
    bot.send_message(message.chat.id, 'Кайфовые скидки на игрульки:', reply_markup=keyboard)
    for key, value in games_sales().items():
        bot.send_photo(message.chat.id, value, caption=key)


def start_shoes(message):
    bot.send_message(message.chat.id, 'Кайфовые скидки на обувь:', reply_markup=keyboard)
    for key, value in shoes_sales().items():
        bot.send_photo(message.chat.id, value, caption=key)


def start_computers(message):
    bot.send_message(message.chat.id, 'Эээээлектроника!!!!! Скидончики!!!!', reply_markup=keyboard)
    for key, value in computer_sales().items():
        bot.send_photo(message.chat.id, value, caption=key)


def start_tours(message):
    bot.send_message(message.chat.id, 'Любите путешествовать!? А Экономить?'
                                      'А вот и скидончики подъехали - дерзайте', reply_markup=keyboard)
    for key, value in tour_sales().items():
        bot.send_photo(message.chat.id, value, caption=key)


def start_sports(message):
    bot.send_message(message.chat.id, 'Спорт? Ну ты красавчек'
                                      'А вот и подарочек!'
                                      'Скидоны от спортивного питания до спорт. инвентаря.'
                                      'Спорт - жизнь!', reply_markup=keyboard)
    for key, value in sport_sales().items():
        bot.send_photo(message.chat.id, value, caption=key)


def start_food(message):
    bot.send_message(message.chat.id, 'Ммммм,вкусно! Сочные скидоны на сочную еду.', reply_markup=keyboard)
    url = 'https://d2halst20r4hcy.cloudfront.net/cab/ead87/826c/40d2/98f7/63f1dd5d656f/original/45184.jpg'
    bot.send_photo(message.chat.id, url)
    for key, value in food_sales().items():
        bot.send_photo(message.chat.id, value, caption=key)


def promo_computers(message):
    bot.send_message(message.chat.id, 'Эээээлектроника!!!!! Промокодики!!!!', reply_markup=keyboard)
    for key, value in computer_promo().items():
        bot.send_photo(message.chat.id, value, caption=key)


def promo_food(message):
    bot.send_message(message.chat.id, 'Ммммм,вкусно! Сочные промокоды на сочную еду.', reply_markup=keyboard)
    url = 'https://d2halst20r4hcy.cloudfront.net/cab/ead87/826c/40d2/98f7/63f1dd5d656f/original/45184.jpg'
    bot.send_photo(message.chat.id, url)
    for key, value in food_promo().items():
        bot.send_photo(message.chat.id, value, caption=key)


def promo_sports(message):
    bot.send_message(message.chat.id, 'Спорт? Ну ты красавчек'
                                      'А вот и подарочек!'
                                      'Промокоды на спортивного питания, спорт. инвентаря и други плюшки.'
                                      'Спорт - жизнь!', reply_markup=keyboard)
    for key, value in sport_promo().items():
        bot.send_photo(message.chat.id, value, caption=key)


def promo_tours(message):
    bot.send_message(message.chat.id, 'Любите путешествовать!? А Экономить?'
                                      'А вот и промокодики подъехали - дерзайте', reply_markup=keyboard)
    for key, value in tour_promo().items():
        bot.send_photo(message.chat.id, value, caption=key)


def promo_auto(message):
    bot.send_message(message.chat.id, 'Кайфовые промокоды для автотоваров:', reply_markup=keyboard)
    for key, value in auto_promo().items():
        bot.send_photo(message.chat.id, value, caption=key)


def promo_clothes(message):
    bot.send_message(message.chat.id, 'Кайфовые промокоды на шмот:', reply_markup=keyboard)
    for key, value in clothes_promo().items():
        bot.send_photo(message.chat.id, value, caption=key)


def promo_games(message):
    bot.send_message(message.chat.id, 'Кайфовые промокоды на игрульки:', reply_markup=keyboard)
    for key, value in games_promo().items():
        bot.send_photo(message.chat.id, value, caption=key)


def promo_shoes(message):
    bot.send_message(message.chat.id, 'Кайфовые промокоды на обувь:', reply_markup=keyboard)
    for key, value in shoes_promo().items():
        bot.send_photo(message.chat.id, value, caption=key)


def send_sticker(message):
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEBEddfFDQHSht4pSb-pGCc2xh-5QkW1AAC4gADCAcCAAHcmz56RDg_WxoE')
    for key, value in cool_sales().items():
        bot.send_photo(message.chat.id, value, caption=key)

bot.polling()
