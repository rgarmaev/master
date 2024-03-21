import telebot
import config
from extensions import CurrencyConverter, APIException

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_instructions(message):
    instructions = "Для получения цены на валюту введите сообщение в формате: <имя валюты, цену которой вы хотите узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>.\n\nДля информации о доступных валютах введите команду /values."
    bot.send_message(message.chat.id, instructions)


@bot.message_handler(commands=['values'])
def send_currency_list(message):
    currency_list = "Доступные валюты:\n1. Евро - EUR\n2. Доллар - USD\n3. Рубль - RUB"
    bot.send_message(message.chat.id, currency_list)


@bot.message_handler(func=lambda message: True)
def convert_currency(message):
    try:
        text = message.text.split()
        if len(text) != 3:
            raise APIException(
                "Неверный формат ввода. Пожалуйста, введите данные в формате <имя валюты> <имя валюты> <количество>")

        base_currency = text[0].upper()
        quote_currency = text[1].upper()
        amount = float(text[2])

        converted_amount = CurrencyConverter.get_price(base_currency, quote_currency, amount)
        bot.send_message(message.chat.id, f"{amount} {base_currency} = {converted_amount} {quote_currency}")

    except APIException as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")


bot.polling()