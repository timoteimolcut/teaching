# #list
# a = [1,2,3,4]
# b = ["1","2","3","4"]
# c = [1,"2",[3,"4"]]
# print(a)
# print(len(b))
# print(b[2])
# print(len(c))
# print(len(c[2]))
# print(c[2])
# a[3] = 10
# print(a)

# #tuple
# d = (1,2,3,4)
# print(d)
# print(len(d))
# print(d[2])
# # d[3] = 10
# # print(d)

# #dictionnary
# e = {1:"a",2:"b",3:"c",4:"d"}
# print(e)
# print(e[1],e[2],e[3],e[4])
# print(e.items())
# print(e.keys())
# print(e.values())

my_dict = dict()
# # my_dict[100] = "q"
# # my_dict[10] = "w"
# # my_dict[1] = "e"

# chars = ["a","b","c","d"]

# for idx, c in enumerate(chars):
#     print(idx, c)

# my_dict.update({1000 : "a"})

string = "Good morning! It's very cold outside. There's some snow too! Yay!"

print(string)
list_of_words = string.split()
print(list_of_words)
print(list(enumerate(list_of_words)))

# type(a) is a way to tell us what kind of data structure it is

for idx, word in enumerate(list_of_words):
    print(idx, word)
    my_dict [idx] = word
print(my_dict)

# What is supposed to work with the above code.
"""Good morning! It's very cold outside. There's some snow too! Yay!
['Good', 'morning!', "It's", 'very', 'cold', 'outside.', "There's", 'some', 'snow', 'too!', 'Yay!']
[(0, 'Good'), (1, 'morning!'), (2, "It's"), (3, 'very'), (4, 'cold'), (5, 'outside.'), (6, "There's"), (7, 'some'), (8, 'snow'), (9, 'too!'), (10, 'Yay!')]
0 Good
1 morning!
2 It's
3 very
4 cold
5 outside.
6 There's
7 some
8 snow
9 too!
10 Yay!

{0: 'Good', 1: 'morning!', 2: "It's", 3: 'very', 4: 'cold', 5: 'outside.', 6: "There's", 7: 'some', 8: 'snow', 9: 'too!', 10: 'Yay!'}"""





#set




"""while
nums = [*range(15)]
# print(nums,len(nums))
# print(nums.pop())
while len(nums) != 0:
    print(nums,len(nums))
    print(nums.pop())
print(nums,len(nums))"""
