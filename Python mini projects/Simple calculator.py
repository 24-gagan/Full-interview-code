def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("1.addition")
print("2.Subtraction")
print("3.Multiplication")
print("4 Division")

choice=int(input("enter the choice"))
num1=int(input("enter first number"))
num2=int(input("enter the second number"))

if choice==1:
    print("Addition of two numberss",add(num1,num2))

elif choice==2:
    print("Subtraction of two numbers",sub(num1,num2))

elif choice==3:
    print("multiplication of two numbers",mul(num1,num2))

elif choice==4:
    print("division of two numbers",div(num1,num2))

else:
    print("invalid choice")