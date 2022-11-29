from sys import platform
from pathlib import Path
from time import sleep as wait
from os import path

from selenium import webdriver as web
from selenium.webdriver.common.by import By

from url_builder import JuneURL

PLATFORMS_DRIVER = {"win32": "chromedriver.exe", "linux": "chromedriver_linux"}
BASE_DIR = Path(__file__).resolve().parent
CHROME_DRIVER_PATH = path.join(BASE_DIR, PLATFORMS_DRIVER.get(platform))

options = web.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--desable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


def pars_hh():
    """Функция парсинга сайта hh.

        Возвращает None в случае если ничего не найдено, либо 
    словарь вида {"vacancy":{
                    "link":<ссылка на вакансию>,
                    "description":<описание вакансии>
                    }
                }
    """
    driver = web.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)
    url = JuneURL()
    driver.get(url.text_url)
    wait(5)
    result_header = driver.find_element(
        By.CLASS_NAME, 'bloko-header-section-3'
    )
    if 'ничего не найдено' in result_header.text.lower():
        return None
    vacancy_block = driver.find_element(By.CLASS_NAME, 'vacancy-serp-content')
    vacancys = vacancy_block.find_elements(By.CLASS_NAME, 'serp-item')
    result = tuple()
    for vacancy in vacancys:
        link = vacancy.find_element(
            By.CLASS_NAME, 'serp-item__title'
        ).get_attribute('href')
        description = vacancy.text
        # фильтруем попавшиеся senior ваканскии (пока рано на них смотреть)
        if 'senior' in description.lower():
            continue
        milled_description = _remove_extra_data(description)
        result = result + ({'link': link, 'description': milled_description},)
    driver.quit()
    return result


def _remove_extra_data(text):
    """Функция удаления лишних строк по шаблону из описания вакансий."""
    text = text.strip()
    templates_for_removing = (
        'Откликнуться', 'Показать контакты', 'Будьте первыми', 'Можно из дома',
        'Работодатель сейчас онлайн', 'Отклик без резюме'
    )
    for template in templates_for_removing:
        text = text.replace(template, '')
    return text
