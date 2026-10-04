num = 20

square = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(1, num))))
print(square)
