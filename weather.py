# Погода
def getWeather(message, city, bot):
	from pyowm import OWM
	from pyowm.utils import config
	from pyowm.utils import timestamps
	from pyowm.utils.config import get_default_config

	bot.send_chat_action(message.chat.id, 'typing')
	
	try:
		config_dict = get_default_config()
		config_dict['language'] = 'ru'
		owm = OWM("86f66426b23488991870e99f0b90d48b", config_dict)
		mgr = owm.weather_manager()
		observation = mgr.weather_at_place( city )
		w = observation.weather
		bot.reply_to(message, "Погода в городе " + city + ": " + str( w.temperature('celsius')['temp']) )
	except Exception as e:
		print("Ошибка:", e)
		pass

# Погода
def dialog(message, bot, types):
	markup = types.InlineKeyboardMarkup(row_width=2)
	item1 = types.InlineKeyboardButton("В Киевском", callback_data='weather.home')
	item2 = types.InlineKeyboardButton("В Красноярске", callback_data='weather.another')

	markup.add(item1, item2)

	bot.send_message(message.chat.id, 'В каком городе?', reply_markup=markup)
