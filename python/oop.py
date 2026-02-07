
import time as t
from time import time

class BankAccount:
    """predefined, but overwritten"""
    def __init__(self, owner_to_be_added="Alice", balance_to_be_added=123, deposit_timestamps=[]): #constructor
        self.owner = owner_to_be_added
        self.balance = balance_to_be_added
        self.deposit_timestamps = deposit_timestamps #property

    """not predefined"""
    def deposit(self, amount=100): #method
        self.balance += amount
        formatted_time = t.strftime('%Y-%m-%d %H:%M:%S', t.gmtime(time()))
        self.deposit_timestamps.append(formatted_time)
        # += == self.balance + amount 

    def withdraw(self, amount=10):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount
    
    def __str__(self): #to string
        times = ""
        for d_time in self.deposit_timestamps:
            times += d_time + "\n"
        return f"{self.owner}: {self.balance} € \n{times}"

account1 = BankAccount("Alice", 200)
print(account1.owner)
print(account1.balance)
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

print("__________________________")

account2 = BankAccount("Alice", 1000)
print(account2)
take_amount = 2000
BankAccount.withdraw(account2, take_amount)
print(account2)
print(type(account2))




