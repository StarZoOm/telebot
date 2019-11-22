from Bot.config import TOKEN
import telebot
from telebot import apihelper
apihelper.proxy = {'https': 'socks5://defaultproxyuser2:nwqCxPM6TCEXG8d@socks5.momentum.rest:1080'}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'ПОДЪЁЁЁЁЁЁМ!')

bot.polling()