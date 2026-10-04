list1 = [1, 2, 3, 2, 1]
list2 = str(list1)
rev = ""
for i in list2:
    rev = rev + i
if rev == list2:
    print("Palidrome")
else:
    print("Not a palidrome")
