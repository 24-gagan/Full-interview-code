def my_decorators(func):
    def wrapper(*args,**kwargs):
        print("First program")
        func()
        print("second program")
    return wrapper
@my_decorators
def say_hello():
    print("say hello")
say_hello()