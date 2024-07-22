import telebot
import random

API_TOKEN = '7188153250:AAFkR1jKkTDaPyfnX2NKhX2B2ToIGEYItRI'

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcom(message):
    bot.reply_to(message, f'Добро пожоловать в бот "bot name" v0.1')

@bot.message_handler(commands=['help'])
def send_help(message):
    help_txt = (
        "<b>Доступные каманды:</b>\n"
        "/help - Ввыводит все камманды\n"
        "/start - Запустит бота\n"
        "/rand - отправка случайной картинки\n"

    )
    bot.reply_to(message, help_txt)

@bot.message_handler(commands=['rand'])
def rand_img(message):
    try:
        random_index = random.randint(0,1)
        image_path = f"./img/image{random_index}.jpg"
        with open(image_path, 'rb') as image_file:
            bot.send_photo(message.chat.id, image_file)
    except Exception as e:
        bot.reply_to(message, f"false {e}")

@bot.message_handler()
def handle_unknown_command(message):
    bot.reply_to(message, "<b>Я не хочу разгаваривать на эту тему</b>")



bot.polling()