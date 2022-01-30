from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from Configs import translations


class SerialCallback:
    def __init__(self):
        self.generate_serial_inline()
    
    def generate_serial_inline(self):
        self.random_serial_inline_data = CallbackData("button", "category")

        self.random_serial_inline_btns = {
            "fantastic": InlineKeyboardButton(
                text=translations.get('callbacks.serial.fantastic'), 
                callback_data=self.random_serial_inline_data.new(
                    category="fantastic",
                )),
            "comedy": InlineKeyboardButton(
                text=translations.get('callbacks.serial.comedy'), 
                callback_data=self.random_serial_inline_data.new(
                    category="comedy",
                )),
            "science": InlineKeyboardButton(
                text=translations.get('callbacks.serial.science'), 
                callback_data=self.random_serial_inline_data.new(
                    category="science",
                )),
        }
        
        self.serial_inline = InlineKeyboardMarkup(row_width=3)
        self.serial_inline.insert(self.random_serial_inline_btns["fantastic"])
        self.serial_inline.insert(self.random_serial_inline_btns["comedy"])
        self.serial_inline.insert(self.random_serial_inline_btns["science"])