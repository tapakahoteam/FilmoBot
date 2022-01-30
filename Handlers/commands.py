from aiogram import types

from Settings import settings
from Configs import translations
from Keyboards import commands_keyboards


# <<<<<<<<<<<<<<<<<< Command [/start] >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["start"])
async def command_start_example(message: types.Message):
    await message.answer(
        translations.get('answers.start').format(
            user_name=message['from']['first_name'], 
            bot_name=(await settings.bot.get_me()).first_name
        ),
        reply_markup=commands_keyboards.start,
        parse_mode="Markdown"
    )