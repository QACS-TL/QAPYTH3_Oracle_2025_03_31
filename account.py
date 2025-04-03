class Account:
    def __init__(self, name, number="111111"):
        self.name = name
        self.number = number
        self._balance = 0

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance < 0:
            balance = 0
        self._balance = balance

    balance = property(get_balance, set_balance)

    def credit(self, amount):
        self._balance += amount
        return f"{self.name} Number {self.number}. New balance {self._balance}"

    def debit(self, amount):
        self._balance -= amount
        return f"{self.name} Number {self.number}. New balance {self._balance}"

    def __str__(self):
        return f"Account No: {self.number} held by {self.name}, has a balance of {self._balance}."
