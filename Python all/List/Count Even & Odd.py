list1 = [1, 2, 3, 4, 5, 6]
count = 0
even = 0
odd = 0
for i in list1:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even count", even)
print("Odd count", odd)
