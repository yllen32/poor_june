from time import sleep

from db_handler import add_vacancys
from hh_parser import pars_hh
from bot import send_new_vacancy

from log import logger


@logger.catch
def check_vacancy():
    try:
        vacancys = pars_hh()
    except Exception as err:
        logger.error(f'Ошибка при парсинге hh - {err}')
    new_vacancy = add_vacancys(vacancys)
    if new_vacancy is None:
        return None
    send_new_vacancy(new_vacancy)


if __name__ == "__main__":
    logger.info('Программа запущена')
    while True:
        logger.info('Ищем вакансии')
        check_vacancy()
        sleep(60*5)  # 5 минут
