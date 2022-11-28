from sys import platform
from pathlib import Path
from time import sleep as wait
from os import path

from selenium import webdriver

PLATFORMS_DRIVER = {"win32": "chromedriver.exe", "linux": "chromedriver_linux"}
BASE_DIR = Path(__file__).resolve().parent
CHROME_DRIVER_PATH = path.join(BASE_DIR, PLATFORMS_DRIVER.get(platform))
HH_URL = "http://usmt.mcx.ru/RequestInformation/Page?p=1"


options = webdriver.ChromeOptions()

#options.add_argument('--headless')
options.add_argument('--desable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')

