class Dog:
    def bark(self):
        return "Woof"
def new_bark(self):
    return "Meow"
Dog.bark=new_bark
dog=Dog()
print(dog.bark())