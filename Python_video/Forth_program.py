# Second largest element in a list
numbers = [1, 4, 3, 5, 2, 6]
first = second = float("-inf")
for number in numbers:
    if number > first:
        second = first
        first = number
    elif number > second and number != first:
        second = number
print("Socond largest number is", second)
