list1 = [1, 2, 2, 3, 4, 3]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print("Removing duplicates", list2)
