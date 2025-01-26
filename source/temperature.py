import os
import requests
import json
from langdetect import detect
from googletrans import Translator

from utils.language import translate_description
from utils.weather import fetch_weather
from config import bot, WEATHER_API_KEY

# Dictionary to track the state of each user, based on their chat ID
user_states = {}


def temperature_command(message):
    bot.send_message(
        message.chat.id,
        "Send me the name of your city and I'll give you the weather forecast for the day!😃"
    )

    # Update the user's state to indicate they are now waiting for the city input
    user_states[message.chat.id] = 'waiting_for_city'

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'waiting_for_city')
def get_city_weather(message):
    city = message.text.strip()

    # Check if the city name is empty or invalid
    if not city:
        bot.reply_to(
            message,
            "❌ Please provide the name of a city to get the weather forecast!"
        )
        return

    # Remove the user's state after processing the city
    user_states.pop(message.chat.id, None)

    # Language detection
    try:
        language = detect(city)
    except Exception:
        language = 'en'

    try:
        data = fetch_weather(city)

        if data is None:
            # If no data is returned (city not found), inform the user
            bot.reply_to(
                message,
                f"❌ Sorry, I couldn't find the city '{city.capitalize()}' on the website. Please make sure the name is correct and try again."
            )
        else:
            # Translate weather description
            weather_description = data['weather'][0]['description']
            translated_description = translate_description(weather_description, language)

            # Format weather forecast based on language
            match language:
                case 'uk':  # Ukrainian
                    weather_forecast = (
                        f"🌤 Погода в {city.capitalize()}:\n"
                        f"Температура: {data['main']['temp']}°C\n"
                        f"Відчувається як: {data['main']['feels_like']}°C\n"
                        f"Стан: {translated_description.capitalize()}\n"
                        f"Координати міста {city.capitalize()}:\nШирота: {data['coord']['lat']}\t\tДовгота: {data['coord']['lon']}"
                    )
                case _:  # Default to English
                    weather_forecast = (
                        f"🌤 Weather in {city.capitalize()}:\n"
                        f"Temperature: {data['main']['temp']}°C\n"
                        f"Feels like: {data['main']['feels_like']}°C\n"
                        f"Condition: {data['weather'][0]['description']}\n"
                        f"City coordinates {city.capitalize()}:\nLatitude: {data['coord']['lat']}\t\tLongitude: {data['coord']['lon']}"
                    )

            bot.reply_to(
                message,
                weather_forecast
            )

    except json.JSONDecodeError:
        # If there is a problem with the weather data format, send an error message
        weather_forecast = "❌ Failed to process the weather data. Please try again later."
        bot.reply_to(
            message,
            weather_forecast
        )