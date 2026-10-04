class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def amount(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
obj=Bank(100)
obj.amount(5000)
print(obj.get_balance())