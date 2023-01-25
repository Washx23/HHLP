#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    for c in range(0, len(my_list)):
        if c == idx:
            my_list.remove(c + 1)
            return my_list
