#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        p = my_list[0]
        for n in my_list:
            if n > p:
                p = n
        return p
