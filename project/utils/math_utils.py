
PI = 3.1415

def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

if __name__ == "__main__": # run as script
    print("Entering math.utils script.")
    print(add(2, 2))
else: # imported or "run as module"
    print(f"module {__name__} imported")
    