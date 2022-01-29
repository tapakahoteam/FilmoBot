from aiogram import types

class ExampleKeyboard:
    def __init__(self):
        self.main = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.main.add(types.KeyboardButton(text="Hi"), types.KeyboardButton(text="Joke"))