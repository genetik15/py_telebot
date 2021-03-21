import weather
import telebot
from telebot import types
import random

bot = telebot.TeleBot("1548213505:AAGDxA7SrQIfDz1AsfsSk14PSwTLOnMtClo", parse_mode=None)

@bot.message_handler(content_types=['sticker'])
def sticker(message):
	print(message)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/night_wolf.jpg', 'rb')
	bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAP-YDv9QfE2w6YSHILXUrfHOJT2LRcAAlkJAAIItxkCTx9qyh5xtYEeBA')
 
	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🎲 Рандомное число")
	item2 = types.KeyboardButton("😊 Как дела?")
	item3 = types.KeyboardButton("🌡️ Узнать погоду?")
 
	markup.add(item1, item2, item3)
 
	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

	
@bot.message_handler(content_types=['text'])
def send_echo(message):
	text = message.text
	if message.chat.type == 'private':
		if text == '🌡️ Узнать погоду?':
			weather.dialog(message, bot, types)
		elif text == '🎲 Рандомное число':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
		elif text == '😊 Как дела?':
 
			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
			item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
			markup.add(item1, item2)
 
			bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')       
	else:       
		bot.send_message(message.chat.id, text)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
			elif call.data == 'weather.home':
				weather.getWeather(call.message, 'Киевский', bot)
			elif call.data == 'weather.another':
				weather.getWeather(call.message, 'Красноярск', bot)
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'Бывает 😢')
 
			# remove inline buttons
			# bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
				# reply_markup=None)
 
			# show alert
			# bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
				# text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
 
	except Exception as e:
		print(repr(e))

bot.polling( none_stop = True)


