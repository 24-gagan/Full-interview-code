numbers = [4, 7, 2, 9, 5]
first = second = float("-inf")
for number in numbers:
    if number > first:
        second = first
        first = number
    elif number > second and number != first:
        second = number
print("Second number is", second)
