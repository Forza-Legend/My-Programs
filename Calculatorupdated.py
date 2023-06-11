import math
import os

print("    ")
os.system('CLS')

# This function adds two numbers
def add(x, y):
    print(x + y)

# This function subtracts two numbers
def subtract(x, y):
    print(x - y)

# This function multiplies two numbers
def multiply(x, y):
    print(x * y)

# This function divides two numbers
def divide(x, y):
    print(x / y)

# This function finds the root of a number
def root(x, y):
    print(x**(1/y))

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Radical")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4' , '5'):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print(x, "+", y, "=", add(x, y))

        elif choice == '2':
            print(x, "-", y, "=", subtract(x, y))

        elif choice == '3':
            print(x, "*", y, "=", multiply(x, y))

        elif choice == '4':
            print(x, "/", y, "=", divide(x, y))
        
        elif choice == '5':
            a = root(x, y)
            print(f"The {y}th root of {x} is {a}")
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
