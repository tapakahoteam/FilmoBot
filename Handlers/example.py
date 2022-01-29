from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types.inline_keyboard import InlineKeyboardMarkup

from Settings import settings
from Callbacks import example_callback
from Keyboards import example_keyboard

# ! TODO: add languages file


# <<<<<<<<<<<<<<<<<< Command [answering with keyboard] >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["start"])
async def command_example(message: types.Message):
    await message.answer("/start works!!!", reply_markup=example_keyboard.main)


# TODO: move inline into service
# <<<<<<<<<<<<<<<<<< Command with callback >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["help"])
async def command_example(message: types.Message):

    inline = InlineKeyboardMarkup(row_width=3)
    inline.insert(example_callback.example_callback_btns["1"])
    inline.insert(example_callback.example_callback_btns["2"])
    inline.insert(example_callback.example_callback_btns["3"])
    inline.insert(example_callback.example_callback_btns["A"])
    inline.insert(example_callback.example_callback_btns["B"])
    inline.insert(example_callback.example_callback_btns["C"])

    await message.answer("/help works!!!", reply_markup=inline)


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=number] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(example_callback.example_callback_data.filter(type="number"))
async def callback_number_example(call: types.CallbackQuery, callback_data: dict):
    await call.message.edit_text(f"Number value: {callback_data['value']}")


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=letter] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(example_callback.example_callback_data.filter(type="letter"))
async def callback_letter_example(call: types.CallbackQuery, callback_data: dict):
    await call.message.edit_text(f"Letter value: {callback_data['value']}")


# <<<<<<<<<<<<<<<<<< Message with filters by many words >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals=['hi', 'hello'], ignore_case=True))
async def hello_message_example(message: types.Message):
    await message.answer("Hello!!!")


# <<<<<<<<<<<<<<<<<< Message with filters by one word >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals='joke', ignore_case=True))
async def joke_message_example(message: types.Message):
    await message.answer("<<Funny joke>>")


# <<<<<<<<<<<<<<<<<< Any another message >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler()
async def any_message_handler_example(message: types.Message):
    await message.answer("Sorry, i don't understand, type /start or /help")