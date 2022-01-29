from aiogram.types.inline_keyboard import InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


class ExampleCallback:
    def __init__(self):
        self.example_callback_data = CallbackData("button", "type", "value")
        self.example_callback_btns = {
            "1": InlineKeyboardButton(
                text="№1", 
                callback_data=self.example_callback_data.new(
                    type="number",
                    value="1"
                )),
            "2": InlineKeyboardButton(
                text="№2", 
                callback_data=self.example_callback_data.new(
                    type="number",
                    value="2"
                )),
            "3": InlineKeyboardButton(
                text="№3", 
                callback_data=self.example_callback_data.new(
                    type="number",
                    value="3"
                )),
            "A": InlineKeyboardButton(
                text="A", 
                callback_data=self.example_callback_data.new(
                    type="letter",
                    value="A"
                )),
            "B": InlineKeyboardButton(
                text="B", 
                callback_data=self.example_callback_data.new(
                    type="letter",
                    value="B"
                )),
            "C": InlineKeyboardButton(
                text="C", 
                callback_data=self.example_callback_data.new(
                    type="letter",
                    value="C"
                )),
        }