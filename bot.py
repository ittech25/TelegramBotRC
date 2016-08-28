#!/usr/bin/python3
# -*- coding: utf-8 -*-
import config
import telebot
import logging
from subprocess import call, check_output

bot = telebot.TeleBot(config.token)
logger = telebot.logger

@bot.message_handler(commands=['torrent'])
def add_torrent(message):
    if(len(message.text[8:]) <8):
        out = check_output('transmission-remote -n \'transmission:transmission\' -l',shell=True)
    else:
        try:
            out = call('transmission-remote -n \'transmission:transmission\' -a ' + message.text[8:],shell=True)
        except Exception:
            out = "Ошибка добавления торрента, возможно ссылка имеет не верный формат!"
    bot.send_message(message.chat.id, out)

@bot.message_handler(commands=['screenshot'])
def take_screenshot(message):
    call('scrot 1.png -e \'mv $f /tmp/screen.png\'',shell=True)
    screenshot = open('/tmp/screen.png', 'rb')
    bot.send_photo(message.chat.id,screenshot)   

@bot.message_handler(commands=['cmd'])
def run_command(message):
    if(message.chat.id!= 114959131):
        return
    try:
        out = check_output(message.text[5:], shell=True)
    except Exception:
        out = "Возникла ошибка выполнения!"
    bot.send_message(message.chat.id, out)


if __name__ == '__main__':
    bot.polling(none_stop=True)
