import random
import string


def generate_random_string(length):
    if length < 4:
        return "Ошибка! Длина должна быть минимум 4 символа."

    digits = random.choice(string.digits)
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    special_characters = random.choice("!#%:,.;*()[]{}<>/?@&-=+")

    remaining_chars = random.choices(
        string.ascii_letters + string.digits + "!#%:,.;*()[]{}<>/?@&-=+", k=length - 4
    )

    result_list = list(digits + uppercase + lowercase + special_characters + "".join(remaining_chars))
    random.shuffle(result_list)

    return "".join(result_list)


try:
    length = int(input())
    if length < 1:
        raise ValueError
    result = generate_random_string(length)
    print(result)
except ValueError:
    print("Ошибка! Введите положительное целое число.")

