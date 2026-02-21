
import time as t
from time import time

# Python generic class is the object in which BankAccount is found
class BankAccount:
    """predefined, but overwritten"""
    def __init__(self, owner_to_be_added="Alice", balance_to_be_added=123, deposit_timestamps=[]): #constructor
        self.owner = owner_to_be_added
        self.balance = balance_to_be_added
        self.deposit_timestamps = [] #deposit_timestamps #property

    """not predefined"""
    def deposit(self, amount=100): #method
        print(f"Start deposit : {self.balance}, {amount}")
        self.balance += amount
        t.sleep(amount//20)
        print(f"End deposit : {self.balance}")
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
    
#inheritance
class SavingsAccount(BankAccount):
    def __init__(self, owner="Alice", balance=123, interest_rate=3.0): #owner is the parameter
            super().__init__(owner, balance)
            self.interest_rate = interest_rate #the first interest rate is an attribute
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate/100

    
dummy = "inheritance"

if dummy != "inheritance":
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
else:
    save_account = SavingsAccount()
    print(save_account)
    n = 50
    for i in range(n):
        save_account.apply_interest()
        print(save_account)



# import time
# time.sleep(2)
# print("Hello"); time.sleep(2); print("How are you ?")
# Hello
# # How are you ?
