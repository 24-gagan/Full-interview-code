num=153
sum=0
temp=num
while num>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if sum==num:
    print("number is a armstrong number")
else:
    print("number is not a armstrong number")