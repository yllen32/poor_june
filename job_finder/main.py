from hh_parser import pars_hh
from db_handler import add_vacancys
from bot import send_new_vacancy


def check_vacancy():
    vacancys = pars_hh()
    new_vacancy = add_vacancys(vacancys)
    if new_vacancy is None:
        return None
    send_new_vacancy(new_vacancy)


if __name__ == "__main__":
    check_vacancy()
