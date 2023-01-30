#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    aux = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            aux += 1
        except (ValueError, TypeError):
            pass
    print()
    return aux