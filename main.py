import os
from dotenv import load_dotenv

import telebot
import webbrowser


load_dotenv()
bot = telebot.TeleBot(os.environ["API_KEY"])


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

@bot.message_handler(commands=['test'])
def take_english_test(message):
    message_to_user = "*Test:*\n[Click here to take the test](https://test-english.com/level-test/) 😉"
    bot.send_message(message.chat.id, message_to_user, parse_mode='MarkdownV2')


@bot.message_handler(commands=['help'])
def main(message):
    message_to_user = "*Help:*\nThis bot can serve you"
    bot.send_message(message.chat.id, message_to_user, parse_mode='MarkdownV2')


@bot.message_handler(commands=['menu'])
def menu(message):
    markup = telebot.types.InlineKeyboardMarkup()

    # Create Inline buttons
    markup.row(
        telebot.types.InlineKeyboardButton('English language test', url='https://test-english.com/level-test/'),
    )

    # Replace KeyboardButton with InlineKeyboardButton for levels
    markup.row(
        telebot.types.InlineKeyboardButton('A1 level', callback_data='A1', url="https://test-english.com/vocabulary/a1/"),
        telebot.types.InlineKeyboardButton('A2 level', callback_data='A2', url="https://test-english.com/vocabulary/a2/")
    )

    markup.row(
        telebot.types.InlineKeyboardButton('B1 level', callback_data='B1', url="https://test-english.com/vocabulary/b1/"),
        telebot.types.InlineKeyboardButton('B2 level', callback_data='B2', url="https://test-english.com/vocabulary/b2/")
    )

    markup.row(
        telebot.types.InlineKeyboardButton('C1 level', callback_data='C1', url="https://test-english.com/vocabulary/c1/")
    )

    # Send the message with the inline keyboard
    bot.send_message(
        message.chat.id,
        message_to_user,
        parse_mode='MarkdownV2',
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    message = callback.message
    data = callback.data

    match data:
        case 'delete':
            bot.delete_message(message.chat.id, message.message_id - 1)
            bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(content_types=['photo', 'video', 'voice', 'video_note'])
def get_media(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Go to google', url="https://www.google.com/"))
    markup.add(telebot.types.InlineKeyboardButton(f'Delete this {message.content_type}', callback_data='delete'))

    match message.content_type:
        case 'photo':
            bot.reply_to(message, "Sorry, I don't accept photo!", reply_markup=markup)

        case 'video':
            bot.reply_to(message,"Sorry, I don't accept video!",reply_markup=markup)

        case 'voice':
            bot.reply_to(message,"Sorry, I don't accept voice messages!",reply_markup=markup)

        case 'video_note':
            bot.reply_to(message,"Sorry, I don't accept video notes!",reply_markup=markup)


@bot.message_handler(content_types=['video'])
def get_video(message):
    bot.reply_to(message, "Sorry, I don't accept photo!")





# For looping
bot.polling(none_stop=True)