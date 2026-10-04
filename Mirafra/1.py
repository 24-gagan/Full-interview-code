def my_decorators(func):
    def wrapper():
        print("First program")
        func()
        print("Second program")

    return wrapper


@my_decorators
def say_hello():
    print("Say HEllo")


say_hello()
