from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


class ExampleCallback:
    def __init__(self):
        self.generate_example_inline()
    
    def generate_example_inline(self):
        self.example_inline_data = CallbackData("button", "type", "value")

        self.example_inline_btns = {
            "1": InlineKeyboardButton(
                text="№1", 
                callback_data=self.example_inline_data.new(
                    type="number",
                    value="1"
                )),
            "2": InlineKeyboardButton(
                text="№2", 
                callback_data=self.example_inline_data.new(
                    type="number",
                    value="2"
                )),
            "3": InlineKeyboardButton(
                text="№3", 
                callback_data=self.example_inline_data.new(
                    type="number",
                    value="3"
                )),
            "A": InlineKeyboardButton(
                text="A", 
                callback_data=self.example_inline_data.new(
                    type="letter",
                    value="A"
                )),
            "B": InlineKeyboardButton(
                text="B", 
                callback_data=self.example_inline_data.new(
                    type="letter",
                    value="B"
                )),
            "C": InlineKeyboardButton(
                text="C", 
                callback_data=self.example_inline_data.new(
                    type="letter",
                    value="C"
                )),
        }
        
        self.example_inline = InlineKeyboardMarkup(row_width=3)
        self.example_inline.insert(self.example_inline_btns["1"])
        self.example_inline.insert(self.example_inline_btns["2"])
        self.example_inline.insert(self.example_inline_btns["3"])
        self.example_inline.insert(self.example_inline_btns["A"])
        self.example_inline.insert(self.example_inline_btns["B"])
        self.example_inline.insert(self.example_inline_btns["C"])