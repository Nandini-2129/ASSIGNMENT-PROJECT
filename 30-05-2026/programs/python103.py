def reverse(input_str):
    reversed_str = input_str[::-1].swapcase()
    return reversed_str

input_str = input()
print(reverse(input_str))
