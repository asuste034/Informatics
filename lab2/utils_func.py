import requests

def imba_input(msg: str, wanted_type: object = float) -> object:
    """Вспомогательная функция. Проверка на нужный формат"""
    while True:
        try:
            return wanted_type(input(msg))
        except ValueError:
            print('\033[31m'+f'ERROR: Ты ввел фигню :) Ожидается -> {str(wanted_type)}'+'\033[0m')

def rub_usd():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()
    usd_rate = data["Valute"]["USD"]["Value"]
    return usd_rate
