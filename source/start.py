import telebot
from config import TELEGRAM_BOT_API_KEY

bot = telebot.TeleBot(TELEGRAM_BOT_API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    message_to_user = (f"Hello, *{message.from_user.first_name}* 😊")
    with open('images/start_photo.png', 'rb') as file:
        bot.send_photo(
            message.chat.id,
            file,
            message_to_user,
            parse_mode='MarkdownV2'
        )