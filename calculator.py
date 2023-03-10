# Program make a simple calculator

# This function adds two numbers
def add(x,y):
    return x + y

# This function substracts two numbers
def substract(x, y):
    return x - y

# This function divides two numbers
def divide(x,y):
    return x / y

# This function multiplies two numbers
def multiply(x,y):
    return x * y

print('Select operation')
print("1. Add")
print("2. Substract")
print("3. Divide")
print("4. multiply")
print()
while True:
    # Take input from the user
    choice = input("[Enter choice]> ") 
 
    # Check if choice is one of the four options
    if choice in ("1","2","3","4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice =="1":
            print(f"{num1} + {num2} = ", add(num1, num2))
        
        elif choice == "2":
            print(f"{num1} - {num2} = ", substract(num1, num2))

        elif choice == "3":
            print(f"{num1} / {num2} = ", divide(num1, num2))

        elif choice == "4":
            print(f"{num1} * {num2} = ", multiply(num1, num2))
        break
    else:
        print("INVALID INPUT")
