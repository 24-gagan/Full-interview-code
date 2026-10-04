def log_decorator(func):
    def wrapper(*args,**kwargs):
        print("Starting calculation")
        result=func(*args,**kwargs)
        print("Calculation completed")
        return result
    return wrapper
@log_decorator
def add(a,b):
    return a+b
print(add(3,10))