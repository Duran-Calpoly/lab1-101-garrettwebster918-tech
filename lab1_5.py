n = int(input("Enter number: "))

if(n%3 == 0 and n%5 == 0):
    print("It is a multiple")
else:
    print("not a multiple")


n = input("Enter password")
password = "abc123"
if(n == password):
    print("access granted")
else:
    print("access denied")

def calculate_federal_tax(salary):
    if salary <= 11000:
        return salary * 0.10
    elif salary <= 44725:
        return salary * 0.12
    elif salary <= 95375:
        return salary * 0.22
    else:
        return salary * 0.24
