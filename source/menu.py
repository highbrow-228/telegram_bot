import telebot
from config import bot
from source.temperature import temperature_command


def english_menu_command(message):
    markup = telebot.types.InlineKeyboardMarkup()

    markup.row(
        telebot.types.InlineKeyboardButton('English language test', url='https://test-english.com/level-test/'),
    )

    markup.row(
        telebot.types.InlineKeyboardButton('A1 level', callback_data='A1', url="https://test-english.com/vocabulary/a1/"),
        telebot.types.InlineKeyboardButton('A2 level', callback_data='A2', url="https://test-english.com/vocabulary/a2/"),
        telebot.types.InlineKeyboardButton('B1 level', callback_data='B1', url="https://test-english.com/vocabulary/b1/"),
        telebot.types.InlineKeyboardButton('B2 level', callback_data='B2', url="https://test-english.com/vocabulary/b2/"),
    )

    bot.send_message(
        message.chat.id,
        "Please choose your level:",
        parse_mode='MarkdownV2',
        reply_markup=markup
    )

def menu_command(message):
    markup = telebot.types.InlineKeyboardMarkup()

    # Button that sends the /english command
    markup.add(
        telebot.types.InlineKeyboardButton('English', callback_data='english'),
        telebot.types.InlineKeyboardButton('Weather Forecast', callback_data='temperature')
    )

    bot.send_message(
        message.chat.id,
        "Please choose an option:",
        parse_mode='MarkdownV2',
        reply_markup=markup
    )

# Callback handler for the "english" button
@bot.callback_query_handler(func=lambda call: call.data == 'english')
def handle_english(call):
    english_menu_command(call.message)

# Callback handler for the "temperature" button
@bot.callback_query_handler(func=lambda call: call.data == 'temperature')
def handle_temperature(call):
    temperature_command(call.message)