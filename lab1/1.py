def get_position(house):
    return ((house - 1) // 2, house % 2)


def calculate_distance(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))


def find_travel_duration(total_houses, home1, home2):
    if total_houses <= 0:
        return 'Ошибка! Количество домов должно быть больше 0.'
    if home1 <= 0 or home2 <= 0 or home1 > total_houses or home2 > total_houses:
        return 'Ошибка! Введите корректные номера домов.'

    start = (0, 0)
    pos1, pos2 = get_position(home1), get_position(home2)

    if calculate_distance(start, pos1) < calculate_distance(start, pos2):
        first, second = pos1, pos2
    else:
        first, second = pos2, pos1 if home1 > home2 else (pos1, pos2)

    time_to_first = calculate_distance(start, first)
    time_between = calculate_distance(first, second)

    max_x = (total_houses - 1) // 2 if total_houses % 2 else (total_houses // 2) - 1
    exit_time = min(second[0], max_x - second[0])

    return time_to_first + time_between + exit_time


try:
    N = int(input())
    h1 = int(input())
    h2 = int(input())

    result = find_travel_duration(N, h1, h2)
    print(result)
except ValueError:
    print("Ошибка! Введите корректные целые числа.")