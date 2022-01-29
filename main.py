import logging
from aiogram import executor
from Settings import settings

import Handlers

async def on_startup(x):
    logging.info('Bot started')

async def on_shutdown(x):
    logging.info('Bot finished')

if __name__ == '__main__':
    executor.start_polling(settings.dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
    logging.info('Script finished\n')
    

# Не знаю как добавить прощание, или что-то типо того   
# Прокомменитруй что посчитаешь нужным, может что-то лишнее, или чего-то не хватает. 
# Или что переделать может надо, может то, что я написал можно легче и меньше сделать. Ну ты понял вообщем)
import telebot
import config
import random
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('🎲 Рандомный фильм 🎲')
	item2 = types.KeyboardButton('🎲 Рандомный сериал 🎲')
	markup.add(item1, item2)
	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот поможет тебе найти любой фильм 😎".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def repeat(message):
	if message.chat.type == 'private':
		if message.text == '🎲 Рандомный фильм 🎲':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
		elif message.text == '🎲 Рандомный сериал 🎲':
			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Фантастика", callback_data='fantastic')
			item2 = types.InlineKeyboardButton("Комедия", callback_data='comedy')
			item3 = types.InlineKeyboardButton("Научный", callback_data='science')
			markup.add(item1, item2, item3)
			bot.send_message(message.chat.id, 'Сейчас найду!', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'Воспользуйтесь кнопками 😢')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'fantastic':
				bot.send_message(call.message.chat.id, 'Затерянные в космосе')
			elif call.data == 'comedy':
				bot.send_message(call.message.chat.id, 'Как я встретил вашу маму')
			elif call.data == 'science':
			    bot.send_message(call.message.chat.id, 'Сквозь пространство и время с Морганом Фрименом')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Что посмотрим?",
				reply_markup=None)
			bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
				text="Приятного просмотра!")
	except Exception as e:
		print(repr(e))

bot.polling(none_stop=True)
