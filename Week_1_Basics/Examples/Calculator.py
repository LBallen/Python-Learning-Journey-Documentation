from setuptools.package_index import egg_info_for_url


def add (a,b):
    return (a + b)
def sub (a,b):
    return (a - b)
def mul (a,b):
    return (a * b)
def div (a,b):
    if b == 0:
        return "You can't divide by zero"
    return (a / b)

#Menu

print("Select Operation")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

while True:
    choice = input("Enter your choice: ")
    if choice in ("1", "2", "3", "4"):
        try:
            input1 = float(input("Enter your first number: "))
            input2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input, please try again")
            continue
        if choice == "1":
            print(f"{input1} + {input2} = {add(input1, input2)}")
        elif choice == "2":
            print(f"{input1} - {input2} = {sub(input1, input2)}")
        elif choice == "3":
            print(f"{input1} * {input2} = {mul(input1, input2)}")
        elif choice == "4":
            print(f"{input1} / {input2} = {div(input1, input2)}")
        continueinput = input("Do you want to continue? (y/n): ")
        if choice == "y":
            continue
        elif choice == "n":
            break
