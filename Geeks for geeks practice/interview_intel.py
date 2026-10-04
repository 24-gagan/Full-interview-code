list1 = [1, 2, 3, 2, 4]
freq = {}
for i in list1:
    freq[i] = freq.get(i, 0) + 1
for i in list1:
    if freq[i] == 1:
        print(i)
        break
    else:
        pass
