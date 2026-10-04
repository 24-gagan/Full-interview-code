import time


def my_decorators(func):
    def wrapper():
        print("First program")
        time.sleep(3)
        result = func()
        print(result)
        print("second program")
        return result

    return wrapper


@my_decorators
def say_hello():
    for i in range(3):
        if i == 2:
            print("Fail")
    return "Done"


say_hello()
