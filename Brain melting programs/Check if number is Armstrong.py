num = 153
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + digit**3
    temp = temp // 10
if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong number")
