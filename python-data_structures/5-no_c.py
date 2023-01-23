#!/usr/bin/python3
def no_c(my_string):
    new = list(my_string)
    for a in new:
        if ord(a) == 99 or ord(a) == 67:
            new.remove(a)
    return "".join(new)
