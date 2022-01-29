from Callbacks import example_callback
from aiogram.types.inline_keyboard import InlineKeyboardMarkup

class ExampleService:
    @staticmethod
    def get_example_inline_callback() -> InlineKeyboardMarkup:
        inline = InlineKeyboardMarkup(row_width=3)

        inline.insert(example_callback.example_callback_btns["1"])
        inline.insert(example_callback.example_callback_btns["2"])
        inline.insert(example_callback.example_callback_btns["3"])
        inline.insert(example_callback.example_callback_btns["A"])
        inline.insert(example_callback.example_callback_btns["B"])
        inline.insert(example_callback.example_callback_btns["C"])

        return inline