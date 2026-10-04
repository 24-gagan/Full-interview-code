num = 987654
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    if digit % 2 == 0:
        sum = sum + digit
    temp = temp // 10
print("even sum", sum)
