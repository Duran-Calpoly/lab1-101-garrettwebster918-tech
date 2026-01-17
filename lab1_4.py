def calculate_average(x, y, z):
    return (x + y + z) / 3

def add_tax(bill_total):
    return bill_total * 1.10

def greet_user():
    name = input("What's your name? ")
    print(f"Hello {name}!")

print(add_tax(3))
print(calculate_average(2,2,3))
greet_user()