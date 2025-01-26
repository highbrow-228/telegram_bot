import requests
import os

from config import WEATHER_API_KEY


def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    result = requests.get(url)

    if result.status_code == 200:
        return result.json()
    else:
        return None