from hh_parser import pars_hh
from db_handler import add_vacancys


def check_vacancy():
    vacancys = pars_hh()
    add_vacancys(vacancys)


check_vacancy()
