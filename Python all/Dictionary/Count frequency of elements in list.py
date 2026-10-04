list1 = [1, 2, 2, 3, 3, 3]  # create a list
freq = {}  # create a dictionary
for i in list1:  # iterate the list
    if i in freq:  # check if the element is present in a dictionary
        freq[i] += 1  # if yes then increment the frequency
    else:
        freq[i] = 1  # if not present then add it with frequency as 1
print(freq)  # print the dictionary
