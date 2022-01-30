from aiogram import types
from aiogram.dispatcher.filters import Text

from Settings import settings
from Configs import translations
from Services import FilmService


# <<<<<<<<<<<<<<<<<< Get random film >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.commands.random-film')))
async def get_random_film(message: types.Message):
    film = FilmService.get_random_film()
    await message.answer(translations.get('answers.random-film').format(film_name=film['name']))