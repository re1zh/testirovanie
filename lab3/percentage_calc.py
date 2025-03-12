def calculate_percentage(number, percent):
    try:
        number = float(number)
        percent = float(percent)
        return (number * percent) / 100
    except ValueError:
        return "Ошибка: некорректный ввод"

num = input("Введите число: ")
perc = input("Введите процент: ")
result = calculate_percentage(num, perc)
print("Результат:", result)