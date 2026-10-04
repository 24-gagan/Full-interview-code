def outer_function(message):
    def inner_function():
        print(message)
    return inner_function
closure_func=outer_function("Hello Closure")
closure_func()