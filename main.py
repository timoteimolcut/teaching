


chars = ['a', 'b', 'c', 'd']

# for idx, c in enumerate(chars):
#     print(idx, c)

my_dict = dict()
# my_dict[100] = 'q'
# my_dict[10] = 'w'
# my_dict[1] = 'e'

string = "Good morning! It's very cold outside. There's some snow too! Yay!"

print(string)
list_of_words = string.split()
print(list_of_words)
print(list(enumerate(list_of_words)))



for idx, word in enumerate(list_of_words):
    print(idx, word)
    my_dict[idx] = word


print()
print(my_dict)
print()


###################################################################################



class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

account1 = BankAccount("Alice", 100)
account2 = BankAccount("Bob")

print(account1.owner)    # Alice
print(account1.balance)  # 100






