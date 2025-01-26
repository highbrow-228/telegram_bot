# import os
# from dotenv import load_dotenv

# import telebot
# import webbrowser

# load_dotenv()
# bot = telebot.TeleBot(os.environ["TELEGRAM_BOT_API_KEY"])

# @bot.message_handler(commands=['start'])
# def start(message):
#     message_to_user = (f"Hello, *{message.from_user.first_name}* 😊")
#     file = open('images/start_photo.png', 'rb')

#     bot.send_photo(
#         message.chat.id,
#         file,
#         message_to_user,
#         parse_mode='MarkdownV2'
#     )

# @bot.message_handler(commands=['test'])
# def take_english_test(message):
#     message_to_user = "*Test:*\n[Click here to take the test](https://test-english.com/level-test/) 😉"
#     bot.send_message(message.chat.id, message_to_user, parse_mode='MarkdownV2')


# @bot.message_handler(commands=['help'])
# def main(message):
#     message_to_user = "*Help:*\nThis bot can serve you"
#     bot.send_message(message.chat.id, message_to_user, parse_mode='MarkdownV2')


# @bot.message_handler(commands=['menu'])
# def menu(message):
#     markup = telebot.types.InlineKeyboardMarkup()

#     # Create Inline buttons
#     markup.row(
#         telebot.types.InlineKeyboardButton('English language test', url='https://test-english.com/level-test/'),
#     )

#     # Replace KeyboardButton with InlineKeyboardButton for levels
#     markup.row(
#         telebot.types.InlineKeyboardButton('A1 level', callback_data='A1', url="https://test-english.com/vocabulary/a1/"),
#         telebot.types.InlineKeyboardButton('A2 level', callback_data='A2', url="https://test-english.com/vocabulary/a2/")
#     )

#     markup.row(
#         telebot.types.InlineKeyboardButton('B1 level', callback_data='B1', url="https://test-english.com/vocabulary/b1/"),
#         telebot.types.InlineKeyboardButton('B2 level', callback_data='B2', url="https://test-english.com/vocabulary/b2/")
#     )

#     markup.row(
#         telebot.types.InlineKeyboardButton('C1 level', callback_data='C1', url="https://test-english.com/vocabulary/c1/")
#     )

#     # Send the message with the inline keyboard
#     bot.send_message(
#         message.chat.id,
#         message_to_user,
#         parse_mode='MarkdownV2',
#         reply_markup=markup
#     )

# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     message = callback.message
#     data = callback.data

#     match data:
#         case 'delete':
#             bot.delete_message(message.chat.id, message.message_id - 1)
#             bot.delete_message(message.chat.id, message.message_id)

# @bot.message_handler(content_types=['photo', 'video', 'voice', 'video_note'])
# def get_media(message):
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton('Go to google', url="https://www.google.com/"))
#     markup.add(telebot.types.InlineKeyboardButton(f'Delete this {message.content_type}', callback_data='delete'))

#     match message.content_type:
#         case 'photo':
#             bot.reply_to(message, "Sorry, I don't accept photo!", reply_markup=markup)

#         case 'video':
#             bot.reply_to(message,"Sorry, I don't accept video!",reply_markup=markup)

#         case 'voice':
#             bot.reply_to(message,"Sorry, I don't accept voice messages!",reply_markup=markup)

#         case 'video_note':
#             bot.reply_to(message,"Sorry, I don't accept video notes!",reply_markup=markup)


# @bot.message_handler(content_types=['video'])
# def get_video(message):
#     bot.reply_to(message, "Sorry, I don't accept photo!")


# import requests
# import json
# from langdetect import detect
# from googletrans import Translator
# weather_api_key = os.environ["WEATHER_API_KEY"]
# user_states = {}

# @bot.message_handler(commands=['temperature'])
# def temperature(message):
#     bot.send_message(
#         message.chat.id,
#         "Send me the name of your city and I'll give you the weather forecast for the day!😃"
#     )
#     user_states[message.chat.id] = 'waiting_for_city'

# @bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'waiting_for_city')
# def get_city_weather(message):
#     city = message.text.strip().lower()
#     user_states.pop(message.chat.id, None)

#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
#     result = requests.get(url)

#     try:
#         data = json.loads(result.text)
#         if result.status_code == 200:

#             # Визначення мови
#             try:
#                 language = detect(city)  # Визначаємо мову введеного тексту
#             except Exception:
#                 language = 'en'  # За замовчуванням англійська

#             # Ініціалізація перекладача
#             translator = Translator()

#             # Переклад стану погоди на мову користувача
#             weather_description = data['weather'][0]['description']

#             # Переклад стану погоди на мову користувача
#             translated_description = translator.translate(weather_description, dest=language).text

#             # Формуємо прогноз відповідно до мови
#             match language:
#                 case 'uk':  # Українська
#                     weather_forecast = (
#                         f"🌤 Погода в {city.capitalize()}:\n"
#                         f"Температура: {data['main']['temp']}°C\n"
#                         f"Відчувається як: {data['main']['feels_like']}°C\n"
#                         f"Стан: {translated_description.capitalize()}\n"
#                         f"Координати міста {city.capitalize()}:\nШирота: {data['coord']['lat']}\t\tДовгота: {data['coord']['lon']}"
#                     )
#                 case _:  # за замовчуванням англійська
#                     weather_forecast = (
#                         f"🌤 Weather in {city.capitalize()}:\n"
#                         f"Temperature: {data['main']['temp']}°C\n"
#                         f"Feels like: {data['main']['feels_like']}°C\n"
#                         f"Condition: {translated_description.capitalize()}\n"
#                         f"City coordinates {city.capitalize()}:\nLatitude: {data['coord']['lat']}\t\tLongitude: {data['coord']['long']}"
#                     )
#         else:
#             weather_forecast = f"❌ Couldn't fetch weather for {city}. Reason: {data.get('message', 'Unknown error')}"
#     except json.JSONDecodeError:
#         weather_forecast = "❌ Failed to process the weather data. Please try again later."

#     bot.reply_to(
#         message,
#         weather_forecast
#     )


# # For looping
# bot.polling(none_stop=True)