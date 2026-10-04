def number_sequence(n):
    for i in range(n):
        yield i
for num in number_sequence(5):
    print(num)