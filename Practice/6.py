#str1 = "P@#yn26at^&i5ve"
def alphabet(str1):
    count = 0
    for char in str1:
        if char.isalpha():
            count+=1
    print(count)
def digit(str1):
    count = 0
    for char in str1:
        if char.isdigit():
            count+=1
    print(count)
str1 = "P@#yn26at^&i5ve"
alphabet(str1)
digit(str1)


