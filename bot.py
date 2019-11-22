from Bot.config import TOKEN
import telebot
from telebot import apihelper

apihelper.proxy = {'https': 'socks5://defaultproxyuser2:nwqCxPM6TCEXG8d@socks5.momentum.rest:1080'}

bot = telebot.TeleBot(TOKEN)


bot.send_message(480303845, 'i`m fine...')

keyboard_start = telebot.types.ReplyKeyboardMarkup()
keyboard_start.row('Пробуем', 'творить', 'хэрню')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'This is test', reply_markup=keyboard_start)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Твой id = ' + str(message.chat.id))
        print(message)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


@bot.message_handler(content_types=['location'])
def handle_loc(message):
    print(message.location)


if __name__ == '__main__':
    bot.polling()
