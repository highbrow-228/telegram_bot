import telebot

from config import bot
from source.menu import menu_command


def help_command(message):
    message_to_user = """*This bot can do for you:*
    1\\. Help with learning English
    2\\. Tell you what the weather is like in your city

Use the *button below* and choose what you need
Or just type `/` and choose
    """

    markup = telebot.types.InlineKeyboardMarkup()
    menu_button = telebot.types.InlineKeyboardButton(text="Menu", callback_data="menu")
    markup.add(menu_button)

    bot.send_message(
        message.chat.id,
        message_to_user,
        parse_mode='MarkdownV2',
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "menu")
def handle_menu(call):
    menu_command(call.message)