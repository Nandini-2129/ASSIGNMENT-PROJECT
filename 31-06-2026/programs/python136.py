def is_triplet(a, b, c):
    sorted_numbers = sorted([a, b, c])

    return sorted_numbers[0] ** 2 + sorted_numbers[1] ** 2 == sorted_numbers[2] ** 2
print(is_triplet(3, 4, 5))
print(is_triplet(5, 6, 7))
