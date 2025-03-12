EXCHANGE_RATES = {
    "USD": 1.0,
    "EUR": 0.91,
    "RUB": 89.0
}

def convert_currency(amount, from_currency, to_currency):
    try:
        amount = float(amount)
        if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES:
            return "Ошибка: Неизвестная валюта"
        return round(amount * (EXCHANGE_RATES[to_currency] / EXCHANGE_RATES[from_currency]), 2)
    except ValueError:
        return "Ошибка: Некорректный ввод"

amount = input("Введите сумму: ")
from_currency = input("Введите исходную валюту (USD, EUR, RUB): ").upper()
to_currency = input("Введите целевую валюту (USD, EUR, RUB): ").upper()
result = convert_currency(amount, from_currency, to_currency)
print("Результат:", result)