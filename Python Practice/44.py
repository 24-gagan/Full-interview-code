while True:
    try:
        number=int(input("enter a valid number"))
        break
    except ValueError:
        print("Invalid input.Please enter an integer")