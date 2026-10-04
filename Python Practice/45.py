class Product:
    def __init__(self,price):
        self._price=price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        if value>=0:
            self._price=value
        else:
            raise ValueError("Price cannot be negative")
product=Product(50)
print(product.price)
product.price=100
print(product.price)