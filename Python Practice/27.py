def outer_function():
    counter=0
    def inner_function():
        nonlocal counter
        counter+=1
    inner_function()
    return counter
print(outer_function())
counter=0
def increase_counter():
    global counter
    counter+=1
increase_counter()
print(counter)