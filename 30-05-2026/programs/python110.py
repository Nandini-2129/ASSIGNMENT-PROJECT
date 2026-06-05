def index_of_caps(word):
    # Use list comprehension to find indices of capital letters
    return [i for i, char in enumerate(word) if char.isupper()]
print(index_of_caps("eDaBiT"))
