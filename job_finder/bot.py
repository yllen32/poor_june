import os

from dotenv import load_dotenv
from telegram import Bot

from log import logger

load_dotenv()

TOKEN = str(os.getenv('TOKEN'))
USER_ID = os.getenv('USER_ID')

bot = Bot(TOKEN)


def send_new_vacancy(vacancys):
    """Функция отправки свежего сообщения юзеру"""
    quantity = len(vacancys)
    if quantity > 10:
        return logger.warning(f'Слишком много вакансий к отправке- {quantity}')
    for vac in vacancys[0:3]:
        try:
            bot.send_message(USER_ID, f'{vac[0]}\n{vac[1]}')
        except Exception as err:
            logger.critical(f'Ошибка при отправке - {err}')
    logger.info(
                f'Отправлены сообщения с вакансиями в колличестве - {quantity}'
            )
