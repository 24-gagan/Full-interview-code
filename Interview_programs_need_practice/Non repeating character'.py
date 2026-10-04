str1 = "programming"  # create a string
freq = {}  # create a dictionary

for i in str1:
    freq[i] = freq.get(i, 0) + 1  # dicttionary se count melega

for i in str1:  # iterate the string
    if freq[i] == 1:  # checcking the frequency
        print(i)  # printing the character
        break
else:
    pass
