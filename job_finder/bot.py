import os

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

TOKEN = str(os.getenv('TOKEN'))
USER_ID = os.getenv('USER_ID')

bot = Bot(TOKEN)


def send_new_vacancy(vacancys):
    """Функция отправки свежего сообщения юзеру"""
    if len(vacancys) > 10:
        return print('Cлишком много вакансий')
    for vac in vacancys[0:3]:
        bot.send_message(USER_ID, f'{vac[0]}\n{vac[1]}')
