#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    p = number
    p *= -1 
    p %= 10 
    p *= -1
else:
    p = number % 10
if p == 0:
    print(f'Last digit of {number} is {p} and is 0')
elif number < -1:
    print(f'Last digit of {number} is {p} and is less than 6 and not 0')
elif p > 5:
    print(f'Last digit of {number} is {p} and is greater than 5')
elif p < 6 and p != 0:
    print(f'Last digit of {number} is {p} and is less than 6 and not 0')
