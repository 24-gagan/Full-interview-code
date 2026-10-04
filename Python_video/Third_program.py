str1 = "programming"
freq = {}
for i in str1:
    freq[i] = freq.get(i, 0) + 1
for i in str1:
    if freq[i] == 1:
        print(i)
        break
