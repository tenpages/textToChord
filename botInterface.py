import os
import telebot
import configparser

def getBotToken() -> str:
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DEFAULT']['BOT_TOKEN']

BOT_TOKEN = getBotToken()

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
