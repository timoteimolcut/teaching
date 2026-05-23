morning = {"Alice", "Bob", "Charlie"}
afternoon = {"Bob", "Charlie", "Diana"}

only_morning = morning - afternoon
only_afternoon = afternoon - morning
both = morning | afternoon
either = morning & afternoon

print("Workers today:")
for worker in (both):
    print(worker) 

print("------------")

print("Only morning shift workers: ")
for worker in (only_morning):
    print(worker) 

print("------------")


print("Only afternoon shift workers: ")
for worker in (only_afternoon):
    print(worker) 

print("------------")


print("Works morning and afternoon: ")
for worker in (either):
    print(worker) 











