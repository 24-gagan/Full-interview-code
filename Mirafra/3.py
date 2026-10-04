list1 = [1, 2, 3, 4, 5]
k = 2
k = k % len(list1)
result = list1[k:] + list1[:k]
print(result)
