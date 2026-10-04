list1 = [1, 2, 3, 4, 5, 6]
even = []
odd = []
for i in list1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("even", even)
print("odd", odd)
