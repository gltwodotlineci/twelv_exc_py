## Écrivez votre code ici !
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amound must be positive")

        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount > 0 and amount > 0:
            self.balance = self.balance - amount

    def display_balance(self):
        print(f"Welcome Mr/Miss {self.account_holder} you have {self.balance} on your account!")


bianca = BankAccount("Bianca Tropdarg", 10000)
bianca.deposit(1000)
bianca.withdraw(500)
bianca.display_balance()
