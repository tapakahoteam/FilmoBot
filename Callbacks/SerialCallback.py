from aiogram.types.inline_keyboard import InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from Configs import translations


class SerialCallback:
    def __init__(self):
        self.random_serial_callback_data = CallbackData("button", "category")
        self.random_serial_callback_btns = {
            "fantastic": InlineKeyboardButton(
                text=translations.get('callbacks.serial.fantastic'), 
                callback_data=self.random_serial_callback_data.new(
                    category="fantastic",
                )),
            "comedy": InlineKeyboardButton(
                text=translations.get('callbacks.serial.comedy'), 
                callback_data=self.random_serial_callback_data.new(
                    category="comedy",
                )),
            "science": InlineKeyboardButton(
                text=translations.get('callbacks.serial.science'), 
                callback_data=self.random_serial_callback_data.new(
                    category="science",
                )),
        }