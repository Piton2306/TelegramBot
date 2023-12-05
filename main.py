import logging
import time
import os
from  sql import select_last
import telebot
from telebot import apihelper
import logs

title = "Running telegram bot..."
os.system(f"title {title}")
# Logger

TOKEN = '6594195662:AAF0Ssws8t0EzSvnjOpEHymHr4P0L6kgRr8'


# Set proxy

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['price'])
def start_message(message):
    price_old = select_last()
    bot.send_message(message.chat.id, f'{price_old}')



@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, f'https://www.youtube.com/watch?v=iE5fvwLmUGw')

try:
    bot.polling()
except ConnectionResetError:
    message = 'Удаленный хост принудительно разорвал существующее подключение'
    logs.loging('telegram.log', message)
    bot.polling()
except:
    logs.loging('telegram.log')
    bot.polling()



