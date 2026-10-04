list1 = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
freq = {}
for i in list1:
    freq[i] = freq.get(i, 0) + 1
for i in freq:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
