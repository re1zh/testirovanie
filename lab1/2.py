def get_position(house):
    return ((house - 1) // 2, 0 if house % 2 == 1 else 1)

def calculate_distance(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

def compute_total_time(total_houses_str, houses_str):
    if not total_houses_str.isdigit():
        return "Ошибка! Кол-во домов должно быть целым числом."
    total_houses = int(total_houses_str)
    if total_houses <= 0:
        return "Ошибка! Кол-во домов должно быть > 0."

    try:
        house_nums = [int(x) for x in houses_str.split(', ')]
        house_nums = [h for h in house_nums if h != 1]
    except Exception:
        return "Ошибка! Номер дома должен быть целым числом."

    if any(h <= 0 for h in house_nums):
        return "Ошибка! Номер дома должен быть > 0."
    if any(h > total_houses for h in house_nums):
        return "Ошибка! Номер дома не должен быть > кол-ва домов."

    even_list = [h for h in house_nums if h % 2 == 0]
    odd_list = [h for h in house_nums if h % 2 != 0]

    unique_evens = []
    seen = set()
    for h in even_list:
        if h not in seen:
            seen.add(h)
            unique_evens.append(h)
    unique_evens = sorted(unique_evens, reverse=True)

    even_time = 0
    position = (0, 0)
    for num in unique_evens:
        new_pos = get_position(num)
        even_time += calculate_distance(position, new_pos)
        position = new_pos

    from collections import Counter
    even_counts = Counter(even_list)
    extra_even = sum(2 * (cnt - 1) for cnt in even_counts.values())

    unique_odds = []
    seen.clear()
    for h in odd_list:
        if h not in seen:
            seen.add(h)
            unique_odds.append(h)

    if unique_odds:
        mid_val = (total_houses // 2) if total_houses % 2 == 0 else ((total_houses + 1) // 2)
        upper_group = [h for h in unique_odds if h > mid_val]
        lower_group = [h for h in unique_odds if h <= mid_val]
        if len(upper_group) >= len(lower_group):
            unique_odds = sorted(upper_group + lower_group, reverse=True)
        else:
            unique_odds = sorted(upper_group + lower_group)
    else:
        unique_odds = []

    odd_time = 0
    if unique_odds:
        for num in unique_odds:
            new_pos = get_position(num)
            odd_time += calculate_distance(position, new_pos)
            position = new_pos

    odd_counts = Counter(odd_list)
    extra_odd = sum(2 * (cnt - 1) for cnt in odd_counts.values())

    if unique_evens or unique_odds:
        final_house = unique_odds[-1] if unique_odds else unique_evens[-1]
        final_get_position = get_position(final_house)
        if final_get_position[1] == 0:
            max_x = (((total_houses if total_houses % 2 else total_houses - 1) - 1) // 2)
        else:
            max_x = (total_houses // 2 - 1) if total_houses % 2 == 0 else ((total_houses - 1) // 2 - 1)
        exit_time = min(final_get_position[0], max_x - final_get_position[0])
    else:
        exit_time = 0

    total_time = even_time + extra_even + odd_time + extra_odd + exit_time

    all_unique = set(house_nums)
    visited = set(unique_evens + unique_odds)
    unvisited_count = len(all_unique - visited)

    return total_time, unvisited_count

n = input()
s = input()
print(compute_total_time(n, s))
