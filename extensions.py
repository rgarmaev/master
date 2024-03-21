import requests
from config import api_key


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base, symbols, amount):  
        url = "https://api.apilayer.com/exchangerates_data/latest"
        params = {
            'base': base,
            'symbols': symbols
        }
        headers = {
            'apikey': api_key
        }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code != 200:
            raise APIException("Failed to fetch data from API")

        data = response.json()

        if 'error' in data:
            raise APIException(data['error']['info'])

       
        exchange_rate = data['rates'][symbols]
        converted_amount = amount * exchange_rate

        return round(converted_amount, 2)
