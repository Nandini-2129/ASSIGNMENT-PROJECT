def move_to_end(lst, element):
    count = lst.count(element)

    lst = [x for x in lst if x != element]

    lst.extend([element] * count)

    return lst
numbers = [2, 1, 2, 3, 2, 4]
result = move_to_end(numbers, 2)
print(result)
