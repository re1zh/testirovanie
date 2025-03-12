employees = []

def add_employee(name, age, position):
    try:
        age = int(age)
        employees.append({"Имя": name, "Возраст": age, "Должность": position})
        return f"Сотрудник {name} успешно добавлен."
    except ValueError:
        return "Ошибка: Некорректный ввод возраста"

def show_employees():
    if not employees:
        return "Нет сотрудников в базе."
    return "\n".join([f"{e['Имя']}, {e['Возраст']} лет, {e['Должность']}" for e in employees])

while True:
    print("\nМеню:")
    print("1. Добавить сотрудника")
    print("2. Показать сотрудников")
    print("3. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Введите имя: ")
        age = input("Введите возраст: ")
        position = input("Введите должность: ")
        print(add_employee(name, age, position))
    elif choice == "2":
        print(show_employees())
    elif choice == "3":
        break