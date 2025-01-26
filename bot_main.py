import telebot

from source.help import help_command
from source.menu import english_menu_command, menu_command
from source.temperature import temperature_command, get_city_weather
from source.media import handle_media
from source.currency_conversion import convert
from logs.setup_logging import setup_logger
from config import bot


logger = setup_logger()


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
    logger.info(f"Recieve command /start from user @{message.from_user.username}")

@bot.message_handler(commands=['help'])
def help(message):
    help_command(message)
    logger.info(f"Recieve command /help from user @{message.from_user.username}")

@bot.message_handler(commands=['menu'])
def menu(message):
    menu_command(message)
    logger.info(f"Recieve command /menu from user @{message.from_user.username}")

@bot.message_handler(commands=['currency_conversion'])
def currency_conversion(message):
    bot.register_next_step_handler(message, convert)
    bot.send_message(
        message.chat.id,
        "Please enter amount:",
    )

    logger.info(f"Recieve command /currency_conversion from user @{message.from_user.username}")

@bot.message_handler(commands=['english'])
def english_menu(message):
    english_menu_command(message)
    logger.info(f"Recieve command /english from user @{message.from_user.username}")

@bot.message_handler(commands=['temperature'])
def temperature(message):
    temperature_command(message)
    logger.info(f"Recieve command /temperature from user @{message.from_user.username}")

@bot.message_handler(content_types=['photo', 'video', 'voice', 'video_note'])
def media(message):
    handle_media(message)
    logger.info(f"Recieve command media from user @{message.from_user.username}")

@bot.message_handler(func=lambda message: True)
def fallback(message):
    bot.send_message(message.chat.id, "I didn't understand that. Please try again!")
    logger.info(f"Recieve command text from user @{message.from_user.username}")

# Callback handler for the delete button
@bot.callback_query_handler(func=lambda call: call.data == 'delete')
def delete_message(call):
    bot.delete_message(call.message.chat.id, call.message.message_id-1)
    bot.delete_message(call.message.chat.id, call.message.message_id)


# Start polling for messages and callbacks (non-stop)
bot.polling(none_stop=True)