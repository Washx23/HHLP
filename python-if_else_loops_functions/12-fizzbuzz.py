#!/usr/bin/python3
def fizzbuzz():
    for i in range(1,100):
        if i % 15 == 0:
            print("fizzBuzz", end= "")
        elif i % 5 == 0:
            print("Buzz", end= "")
        elif i % 3 == 0:
            print("Fizz", end= "")
        else:
            print (i, end= "")
        if i < 100:
            print(" ", end="")
