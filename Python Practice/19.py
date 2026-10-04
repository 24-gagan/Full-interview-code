class Animal:
    def speak(self):
        return "Animal sound"
class Dog(Animal):
    def speak(self):
        return "Dog sound"
dog=Dog()
print(dog.speak())