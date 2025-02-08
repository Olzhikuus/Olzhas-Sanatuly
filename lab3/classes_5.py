class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, count):
        self.balance += count

    def withdraw(self, count):
        if count > self.balance:
            print("Not enough money")
        else:
            self.balance -= count

user = Account(700)
print(user.balance)
user.deposit(200)
print(user.balance)
user.withdraw(1000)
user.withdraw(100)
print(user.balance)