class MyClass:
    class_variable="Class variable"

    @staticmethod
    def static_method():
        return "This is static method"

    @classmethod
    def class_method(cls):
        return f"This is a class method accessing {cls.class_variable}"
print(MyClass.static_method())
print(MyClass.class_method())