def count_alpha(s):
    count = 0
    for ch in s:
        if ch.isalpha():   # check if character is alphabet
            count += 1
    print("Alphabets count:", count)

def count_digits(s):
    count = 0
    for ch in s:
        if ch.isdigit():   # check if character is digit
            count += 1
    print("Digits count:", count)


str1 = "P@#yn26at^&i5ve"
count_alpha(str1)
count_digits(str1)
