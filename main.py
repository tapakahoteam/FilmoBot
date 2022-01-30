import logging
from aiogram import executor
from Settings import settings

from Handlers import *

async def on_startup(x):
    logging.info('Bot started')

async def on_shutdown(x):
    logging.info('Bot finished')

def start_polling():
    executor.start_polling(settings.dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
    logging.info('Script finished')

if __name__ == '__main__':
    start_polling()