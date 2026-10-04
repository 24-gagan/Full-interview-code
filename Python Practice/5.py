def flatten(nested):
    result = []
    for char in nested:
        if isinstance(char, list):
            result.extend(flatten(char))
        else:
            result.append(char)


print(flatten([1, [2, [3, 4], 5], 6]))
