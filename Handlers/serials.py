from aiogram import types
from aiogram.dispatcher.filters import Text

from Settings import settings
from Configs import translations
from Services import SerialService
from Callbacks import serial_callback

# <<<<<<<<<<<<<<<<<< Get random serial >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.commands.random-serial')))
async def get_random_serial(message: types.Message):
    inline = SerialService.get_random_serial_categories_callback()
    await message.answer(translations.get('answers.random-serial'), reply_markup=inline)


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=number] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(serial_callback.random_serial_callback_data.filter(category="fantastic"))
async def fantastic_serial(call: types.CallbackQuery):
    inline = SerialService.get_random_serial_categories_callback()
    await call.message.edit_text('f', reply_markup=inline)


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=number] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(serial_callback.random_serial_callback_data.filter(category="comedy"))
async def comedy_serial(call: types.CallbackQuery):
    inline = SerialService.get_random_serial_categories_callback()
    await call.message.edit_text('c', reply_markup=inline)


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=number] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(serial_callback.random_serial_callback_data.filter(category="science"))
async def science_serial(call: types.CallbackQuery):
    inline = SerialService.get_random_serial_categories_callback()
    await call.message.edit_text('s', reply_markup=inline)