class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawel amount must be positive")
        if amount > self.balance:
            raise ValueError("Insifficient Fund")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance
