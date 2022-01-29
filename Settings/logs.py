import logging
from os import mkdir

try: mkdir("logs")
except FileExistsError: pass

logging.basicConfig(
    level=logging.DEBUG, 
    handlers=(
        logging.FileHandler('logs/Log.log', mode='a'), 
        logging.StreamHandler()
    ),
    format='[%(asctime)s %(levelname)s] %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S'
)

logging.info('Logging start')