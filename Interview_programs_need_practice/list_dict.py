lst = [1, 2, 3, 4, "a", "b", 4, 5, 6]  # create the list
even_numbers = []  # create two list
odd_numbers = []
for i in lst:  # loop thriugh the list
    if isinstance(i, int):  # check if the element is integer
        if i % 2 == 0:  # check if the element is eve
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
result = dict(zip(even_numbers, odd_numbers))
print(result)
"""In this programing we have to create a dictionary for two list"""
