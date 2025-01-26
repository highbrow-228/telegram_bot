# Telegram Bot

This project is a Telegram bot designed to interact with users in a variety of ways. It provides weather information, handles media inputs, and supports multiple languages for menus and responses. Additionally, it features error handling and fallback options to ensure smooth user interaction.

## Features
- **Start Command**: Greets the user with a personalized message and sends a photo when they start a conversation with the bot.
- **Help Command**: Provides a list of available commands and instructions on how to use the bot.
- **Menu Command**: Displays the main menu with options to interact with the bot.
- **English Menu Command**: Displays the menu in English for users who prefer this language.
- **Temperature Command**: Fetches the weather forecast for a user-provided city, including temperature and weather conditions.
- **Media Handler**: Allows the bot to handle different types of media such as photos, videos, voice messages, and video notes.
- **Fallback Command**: If the bot doesn't understand the user’s message, it will prompt them to try again.

## Requirements
1. Python 3.12.6 or higher
2. Install dependencies from the `requirements.txt` file
3. A `.env` file with necessary API keys

## Installing Dependencies
To install the required libraries, run the following command:
```bash
pip install -r requirements.txt
```

## Setup
### 1. Clone the repository:
First, clone the repository to your local machine:
```bash
git clone git@github.com:highbrow-228/telegram_bot.git
cd telegram-bot
```

### 2. Create a `.env` file:
Create a `.env` file in the root directory and add your Telegram bot API key and OpenWeather API key:
```.env
TELEGRAM_BOT_API_KEY=your-telegram-bot-api-key-here
WEATHER_API_KEY=your-OpenWeather-api-key-here
```

### 3. Install the Dependencies:
Ensure that all the required libraries are installed by running:
```bash
pip install -r requirements.txt
```

### 4. Running the Bot:
Finally, run the bot using the following command:
```bash
python bot_main.py
```
> Note: It is recommended to run the bot in a tmux or screen session to keep it running in the background.

## License
This project is open-source and licensed under the MIT License.