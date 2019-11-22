from Bot.config import TOKEN
import telebot
from telebot import apihelper

apihelper.proxy = {'https': 'socks5://defaultproxyuser2:nwqCxPM6TCEXG8d@socks5.momentum.rest:1080'}

bot = telebot.TeleBot(TOKEN)


bot.send_message(480303845, 'i`m fine...')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'This is test')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Твой id = ' + str(message.chat.id))
        print(message.chat.id)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


if __name__ == '__main__':
    bot.polling()
