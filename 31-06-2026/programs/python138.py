def dict_to_list(input_dict):
    sorted_dict = sorted(input_dict.items())
    result = [(key, value) for key, value in sorted_dict]
    return result
print(dict_to_list({"c": 3, "a": 1, "b": 2}))
