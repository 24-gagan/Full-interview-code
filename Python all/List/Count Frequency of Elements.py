list1 = [1, 2, 2, 3, 3, 3]
freq = {}
for i in list1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Frequency is", freq)
