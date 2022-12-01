
from logging.handlers import RotatingFileHandler

from loguru import logger

from settings import DEBUG_LOG

# дополнительный лог с сбором всей информации уровня DEBAG
if DEBUG_LOG:
    import logging
    handler = RotatingFileHandler(
        'debug.log', maxBytes=50000000, backupCount=5
    )
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
