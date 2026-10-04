class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        return f"{self.brand} {self.model}"
obj=Car("Ford","Mustang")
print(obj.display())