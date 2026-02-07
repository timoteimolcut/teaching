import time as t
from time import time

class BankAccount:
    """predefined, but overwriten"""
    def __init__(self, owner_to_be_added="Alice", balance_to_be_added=123, deposit_timestamps=[]):# constructor
        self.owner = owner_to_be_added
        self.balance = balance_to_be_added
        self.deposit_timestamps = deposit_timestamps # property
    
    def __str__(self):# to string
        times = ""
        for d_time in self.deposit_timestamps:
            times += d_time + "\n"
        return f"{self.owner}: {self.balance} euro \ndeposit timestamps:\n{times}"

    """not predefined"""
    def deposit(self, amount=100):# method
        print(f"Start deposit: {self.balance}, {amount}")
        self.balance += amount
        t.sleep(amount//20)
        print(f"End deposit: {self.balance}")
        formatted_time = t.strftime('%Y-%m-%d %H:%M:%S', t.gmtime(time()))
        self.deposit_timestamps.append(formatted_time)

    def withdraw(self, amount=10):# method
        if self.balance < amount:
            print("Insuficient balance!")
        else:
            self.balance -= amount
    
    
account1 = BankAccount("Bob", 200)
print(account1)
account1.deposit()
print(account1)
account1.deposit()
print(account1)
account1.deposit()
print(account1)
account1.withdraw()
print(account1)
account1.withdraw(900)
print(account1)

print("________")

account2 = BankAccount()
print(account2)
account1.deposit()
print(account1)
take_amount = 2000
BankAccount.withdraw(account2, take_amount)
print(account2)
print(type(account2))














