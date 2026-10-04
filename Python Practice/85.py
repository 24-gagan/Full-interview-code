try:
    z=10/0
except ZeroDivisionError:
    print("exception occured")
else:
    print("if above condition fails this will run")
finally:
    print("so gone")