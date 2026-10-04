try:
    num=int(input("enter a number"))
    print(10/num)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")