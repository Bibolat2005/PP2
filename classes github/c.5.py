class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, cash):
        self.balance += cash
        print(f"Balance: {self.balance}")
    def withdraw(self, cash):
        if self.balance >= cash:
            self.balance -= cash
            print(f"Balance: {self.balance}")
        else:
            print("Not enough balance")
            print(f"Balance: {self.balance}")

acc = Account("John", 0)
acc.deposit(1000)
acc.withdraw(600)
acc.withdraw(700)
acc.deposit(300)
acc.withdraw(700)