import random


def create_random_list():
    return [random.randint(-153, 37) for _ in range(random.randint(10, 30))]


def count_negatives(lst):
    return sum(x < 0 for x in lst)


def modify_signs(lst):
    return [x * (-1 if random.random() < 0.5 else 1) for x in lst]


def process_list(lst):
    even_position_positive_evens = sum(1 for i, x in enumerate(lst) if i % 2 == 0 and x > 0 and x % 2 == 0)
    two_digit_positives = sum(2 for x in lst if 10 <= x <= 99)
    odd_sums_even_positions = sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 != 0)
    return even_position_positive_evens, two_digit_positives, odd_sums_even_positions


numbers = create_random_list()
print("Original list:", numbers)

sign_changes = 0

total_elements = len(numbers)
negative_count = count_negatives(numbers)

with open('output.txt', 'w') as file:
    file.write(" ".join(map(str, numbers)) + '\n')

    while negative_count > total_elements / 2:
        numbers = modify_signs(numbers)
        file.write(" ".join(map(str, numbers)) + '\n')
        negative_count = count_negatives(numbers)
        sign_changes += 1

counts = process_list(numbers)
final_result = sum(counts) * sign_changes

print(f"Result: {final_result}")
