import os
os.system('CLS')
print("")
num = input("Enter the number: ")
num = int(num)
try:
    while num > 1:
        if (num % 2) == 0:
            num = num/2
            print(num)
        else:
            num = num*3+1
            print(num)
finally:
    print("")
    print("<<<<<<<<<< And the 4,2,1 loop continues >>>>>>>>>>")
    print("")
    os.system("looping_equation.py")