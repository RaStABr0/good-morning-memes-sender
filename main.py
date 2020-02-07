from os import listdir
from os.path import isfile
import datetime
import telebot
import sys

TOKEN = '1019784271:AAGTY0SjhOgp5gN1nnHWvTGXbBeSxF9cRPE'
CHAT_ID = '-1001266851208'

PICTURES_PATH = 'C:/Users/babkin_aa/Desktop/Бот'


def main():
    files = get_files()
    bot = telebot.TeleBot(TOKEN)

    bot.send_photo()

    while True:



    return


def get_files():
    files = listdir(PICTURES_PATH)
    for file in files:
        if not isfile(PICTURES_PATH + "\\" + file):
            files.remove(file)
    return files

if __name__ == '__main__':
    main()