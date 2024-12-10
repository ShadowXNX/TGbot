# from telebot import TeleBot
# from telebot import types
import telebot 
from telebot import types 
import sqlite3 as sl
token = 'your token'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'help', 's'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello! Do you have any questions?")
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    button_foo = types.InlineKeyboardButton('Support', callback_data='support')
    button_bar = types.InlineKeyboardButton('Bar', callback_data='bar')
    button_url = types.InlineKeyboardButton('Link', callback_data='link')

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_foo)
    keyboard.add(button_bar)
    keyboard.add(button_url)

    bot.send_message( message.chat.id, text='Keyboard example', reply_markup=keyboard)
@bot.message_handler(commands=['next_button'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)
bot.infinity_polling() 

