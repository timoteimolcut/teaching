
# ── Strings ──────────────────────────────────────────────────────────────────

string = "Good morning! It's very cold outside. There's some snow too! Yay!"

print(string)
list_of_words = string.split()
print(list_of_words)
print(list(enumerate(list_of_words)))


# ── Loops & enumerate ─────────────────────────────────────────────────────────

my_dict = dict()

for idx, word in enumerate(list_of_words):
    print(idx, word)
    my_dict[idx] = word

print()
print(my_dict)
