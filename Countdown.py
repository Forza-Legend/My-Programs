n = 11
n = int(n)
import time
try:
    while True:

        if(n > 0):
            n -= 1
            print(n)
            time.sleep(1)

        if(n == 0):
            print("Time Over")
            time.sleep(1)
            quit()

finally:
    print("")