#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0:
        p = number
        p *= -1
        p %= 10
        p *= -1
    else:
        p = number
        p %= 10
    print("{}".format(p))
    