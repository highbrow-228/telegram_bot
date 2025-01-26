from telebot import types
from config import bot
from currency_converter import CurrencyConverter

currency = CurrencyConverter()
user_amounts = {}  # Create a dictionary to store the amount for each user

# Define supported currencies
SUPPORTED_CURRENCIES = currency.currencies

def convert(message):
    user_id = message.from_user.id

    try:
        # Update the amount value for the current user
        user_amounts[user_id] = float(message.text.strip())
    except ValueError:
        bot.send_message(
            message.chat.id,
            "The format is incorrect. Enter the amount again:"
        )
        bot.register_next_step_handler(message, convert)
        return

    amount = user_amounts[user_id]
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)

        button_1 = types.InlineKeyboardButton('JPY/USD', callback_data=f'JPY/USD|{amount}')
        button_2 = types.InlineKeyboardButton('USD/JPY', callback_data=f'USD/JPY|{amount}')
        button_3 = types.InlineKeyboardButton('USD/EUR', callback_data=f'USD/EUR|{amount}')
        button_4 = types.InlineKeyboardButton('EUR/USD', callback_data=f'EUR/USD|{amount}')

        markup.add(button_1, button_2, button_3, button_4)

        button_5 = types.InlineKeyboardButton('Another pair', callback_data=f'else|{amount}')
        markup.add(button_5)

        bot.send_message(
            message.chat.id,
            "Choose your currency pair for conversion",
            reply_markup=markup
        )
    else:
        bot.send_message(
            message.chat.id,
            "The format is incorrect. The number must be greater than 0. Enter the amount again:"
        )
        bot.register_next_step_handler(message, convert)
        return

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    data = call.data.split('|')

    if data[0] != 'else':
        currency_pair = data[0]
        amount = float(data[1])

        values = currency_pair.upper().split('/')

        # Check if both currencies are supported
        unsupported_currencies = [value for value in values if value not in SUPPORTED_CURRENCIES]

        if unsupported_currencies:
            bot.send_message(
                call.message.chat.id,
                f"Sorry, the currency {', '.join(unsupported_currencies)} is not supported\\. Supported currencies are: `{', '.join(SUPPORTED_CURRENCIES)}`",
                parse_mode='MarkdownV2'
            )
            return

        try:
            result = currency.convert(amount, values[0], values[1])
            bot.send_message(
                call.message.chat.id,
                f"Converting {amount} of the following pair {currency_pair.upper()}: {round(result, 4)}"
            )
        except Exception as e:
            bot.send_message(
                call.message.chat.id,
                f"Something went wrong, exception: {e}"
            )
    else:
        bot.send_message(
            call.message.chat.id,
            "Please enter a currency pair using `/`\\. For example: `USD/EUR`, `USD/JPY`\\.",
            parse_mode='MarkdownV2',
        )
        amount = float(data[1])
        bot.register_next_step_handler(call.message, another_currency, amount, call)

def another_currency(message, amount, call):
    try:
        values = message.text.upper().split('/')
        unsupported_currencies = [value for value in values if value not in SUPPORTED_CURRENCIES]

        if unsupported_currencies:
            bot.send_message(
                message.chat.id,
                f"Sorry, the currencie {', '.join(unsupported_currencies)} is not supported\\. Supported currencies are: `{', '.join(SUPPORTED_CURRENCIES)}`",
                parse_mode='MarkdownV2'
            )
            return

        result = currency.convert(amount, values[0], values[1])

        bot.send_message(
            call.message.chat.id,
            f"Converting {amount} of the following pair {values}: {round(result, 3)}"
        )
    except Exception as e:
        bot.send_message(
            message.chat.id,
            f"Something went wrong, exception: {e}\nTry again:",
        )
        bot.register_next_step_handler(message, another_currency)
