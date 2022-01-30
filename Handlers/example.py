from aiogram import types
from aiogram.dispatcher.filters import Text

from Settings import settings
from Configs import translations
from Services import ExampleService
from Callbacks import example_callback
from Keyboards import example_keyboard


# <<<<<<<<<<<<<<<<<< Command [answering with keyboard] >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["start"])
async def command_start_example(message: types.Message):
    await message.answer(translations.get('start'), reply_markup=example_keyboard.main)


# <<<<<<<<<<<<<<<<<< Command with callback >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["help"])
async def command_help_example(message: types.Message):
    inline = ExampleService.get_example_inline_callback()
    await message.answer(translations.get('help'), reply_markup=inline)


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=number] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(example_callback.example_callback_data.filter(type="number"))
async def callback_number_example(call: types.CallbackQuery, callback_data: dict):
    await call.message.edit_text(translations.get('number-value').format(value=callback_data['value']))


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=letter] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(example_callback.example_callback_data.filter(type="letter"))
async def callback_letter_example(call: types.CallbackQuery, callback_data: dict):
    await call.message.edit_text(translations.get('letter-value').format(value=callback_data['value']))


# <<<<<<<<<<<<<<<<<< Message with filters by many words >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals=['hi', 'hello'], ignore_case=True))
async def hello_message_example(message: types.Message):
    await message.answer(translations.get('hello'))


# <<<<<<<<<<<<<<<<<< Message with filters by one word >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals='joke', ignore_case=True))
async def joke_message_example(message: types.Message):
    await message.answer(translations.get('joke'))


# <<<<<<<<<<<<<<<<<< Any another message >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler()
async def any_message_handler_example(message: types.Message):
    await message.answer(translations.get('dont-understand'))