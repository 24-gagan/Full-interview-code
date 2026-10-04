def calculate(a,b,operation):
    if operation=="add":
        return a+b
    if operation=="subtract":
        return a-b
    if operation=="Multiply":
        return a*b
    elif operation=="divide":
        return a/b if b!=0 else "Division by zero"
print(calculate(10,5,"add"))
print(calculate(10,5,"divide"))