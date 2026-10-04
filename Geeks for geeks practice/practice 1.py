class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog sound")


obj = Dog()
print(obj.sound())
