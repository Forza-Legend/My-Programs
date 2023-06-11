import os
from random import randint

print("Hi")
os.system('CLS')

min_num = int(input("Minimum extreme end: "))
max_num = int(input("Maximum extreme end: "))
ran_num = randint(int(min_num),int(max_num))
print(f"Number: {ran_num}")