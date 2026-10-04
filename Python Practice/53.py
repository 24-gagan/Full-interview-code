class Person:
    __slots__=["name","age"]
    def __init__(self,name,age):
        self.name=name
        self.age=age
person=Person("Alice",10)
print(person.name)