import os
import time

os.system('CLS')

user_input_a = 0
user_input_b = 0
operator = 0
    
while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    
    operator = int(input("Enter choice (1/2/3/4): "))
    user_input_a = float(input("First Number: "))
    user_input_b = float(input("Second Number: "))
    
    if operator == 1:
        print(f"{user_input_a} + {user_input_b} = {user_input_a + user_input_b}")
    
    elif operator == 2:
        print(f"{user_input_a} - {user_input_b} = {user_input_a - user_input_b}")
        
    elif operator == 3:
        print(f"{user_input_a} x {user_input_b} = {user_input_a * user_input_b}")
        
    elif operator == 4:
        print(f"{user_input_a} / {user_input_b} = {user_input_a / user_input_b}")
    
    else:
        print("Invalid input")
        
    another_calculation = input("Lets do another calculation: ")
    
    if another_calculation == "no":
        break