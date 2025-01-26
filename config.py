import os
import telebot
from dotenv import load_dotenv

load_dotenv()

# Bot API key
TELEGRAM_BOT_API_KEY = os.environ["TELEGRAM_BOT_API_KEY"]

# Weather API key
WEATHER_API_KEY = os.environ["WEATHER_API_KEY"]

bot = telebot.TeleBot(os.environ["TELEGRAM_BOT_API_KEY"])