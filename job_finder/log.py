import logging
from logging.handlers import RotatingFileHandler

from loguru import logger

handler = RotatingFileHandler('debug.log', maxBytes=50000000, backupCount=5)

program_log = logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s',
    handlers=(handler,)
)


logger.add(
    "job_finder.log",
    rotation="500 MB",
    format="{time} {level} {message}"
    )