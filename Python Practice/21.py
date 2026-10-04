class MyMeta(type):
    def __new__(cls,name,bases,dct):
        dct["greet"]=lambda self:f"Hello from {name}"
        return super().__new__(cls,name,bases,dct)
class MyClass(metaclass=MyMeta):
    pass
obj=MyClass()
print(obj.greet())