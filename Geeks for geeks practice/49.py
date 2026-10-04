class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance=amount
    def get_balance(self):
        return self.__balance

obj=Bank(100)
print(obj.get_balance())