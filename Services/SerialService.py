from Callbacks import serial_callback
from aiogram.types.inline_keyboard import InlineKeyboardMarkup

class SerialService:
    @staticmethod
    def get_random_serial_categories_callback() -> InlineKeyboardMarkup:
        return serial_callback.serial_inline