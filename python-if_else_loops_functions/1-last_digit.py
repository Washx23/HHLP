#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
p = int(str(number)[-1])
if p == 0:
    print(f'Last digit of {number} is {p} and is 0')
elif number < -1:
    print(f'Last digit of {number} is -{p} and is less than 6 and not 0')
elif p > 5:
    print(f'Last digit of {number} is {p} and is greater than 5')
elif p < 6 and p != 0:
    print(f'Last digit of {number} is {p} and is less than 6 and not 0')
