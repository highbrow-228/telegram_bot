import telebot
from config import bot

def handle_media(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Go to google', url="https://www.google.com/"))
    markup.add(telebot.types.InlineKeyboardButton(f'Delete this {message.content_type}', callback_data='delete'))

    match message.content_type:
        case 'photo':
            bot.reply_to(message, "Sorry, I don't accept photo!", reply_markup=markup)
        case 'video':
            bot.reply_to(message, "Sorry, I don't accept video!", reply_markup=markup)
        case 'voice':
            bot.reply_to(message, "Sorry, I don't accept voice messages!", reply_markup=markup)
        case 'video_note':
            bot.reply_to(message, "Sorry, I don't accept video notes!", reply_markup=markup)
