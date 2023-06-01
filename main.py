#2

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, n):
        print(f'Баланс: {self.balance + n}')
    def withdraw(self, n):
        print(f'Баланс: {self.balance - n}')
b = BankAccount(12, 1000)
n = int(input('Введіть число: '))
b.deposit(n)
b.withdraw(n)