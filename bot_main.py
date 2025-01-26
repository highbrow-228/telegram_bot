import telebot

from source.help import help_command
from source.menu import english_menu_command, menu_command
from source.temperature import temperature_command, get_city_weather
from source.media import handle_media
from config import bot


@bot.message_handler(commands=['start'])
def start(message):
    message_to_user = (f"Hello, *{message.from_user.first_name}* 😊")
    file = open('images/start_photo.png', 'rb')
    bot.send_photo(
        message.chat.id,
        file,
        message_to_user,
        parse_mode='MarkdownV2'
    )

@bot.message_handler(commands=['help'])
def help(message):
    help_command(message)

@bot.message_handler(commands=['menu'])
def menu(message):
    menu_command(message)

@bot.message_handler(commands=['english'])
def english_menu(message):
    english_menu_command(message)

@bot.message_handler(commands=['temperature'])
def temperature(message):
    temperature_command(message)

@bot.message_handler(content_types=['photo', 'video', 'voice', 'video_note'])
def media(message):
    handle_media(message)

@bot.message_handler(func=lambda message: True)
def fallback(message):
    bot.send_message(message.chat.id, "I didn't understand that. Please try again!")

# Callback handler for the delete button
@bot.callback_query_handler(func=lambda call: call.data == 'delete')
def delete_message(call):
    bot.delete_message(call.message.chat.id, call.message.message_id-1)
    bot.delete_message(call.message.chat.id, call.message.message_id)


# Start polling for messages and callbacks (non-stop)
bot.polling(none_stop=True)