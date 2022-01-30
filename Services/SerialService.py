from Callbacks import serial_callback
from aiogram.types.inline_keyboard import InlineKeyboardMarkup

class SerialService:
    @staticmethod
    def get_random_serial_categories_callback() -> InlineKeyboardMarkup:
        inline = InlineKeyboardMarkup(row_width=3)

        inline.insert(serial_callback.random_serial_callback_btns["fantastic"])
        inline.insert(serial_callback.random_serial_callback_btns["comedy"])
        inline.insert(serial_callback.random_serial_callback_btns["science"])

        return inline