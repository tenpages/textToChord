import os
import telebot
from telebot.types import InputFile
import configparser

from textToChord import *

def getBotToken() -> str:
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DEFAULT']['BOT_TOKEN']

BOT_TOKEN = getBotToken()
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello This is a simple bot to add a little sound effect to your chat. To play a certain chord, type \"/d\" + \"The name of the cord\". For example, \"/d Cmaj7\".")

@bot.message_handler(commands=['d'])
def send_chord(message):
    order_text = message.text
    chord_in_text, chord_loc = parseRequest(order_text+" 4")
    chat_id = message.chat.id
    print(message, message.id, message.chat, message.chat.id)
    print(chord_loc)
    bot.send_voice(chat_id, InputFile(chord_loc), caption=chord_in_text, reply_to_message_id = message.id)
    os.remove(chord_loc)

bot.infinity_polling()
