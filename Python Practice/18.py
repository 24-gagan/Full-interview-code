try:
    z=10/0
except ZeroDivisionError:
    print("Zerodivision error occured")
else:
    print("Division successfull")
finally:
    print("Execution completed")