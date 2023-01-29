#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = list(set_1) + list(set_2)
    dup = {x for x in new_list if new_list.count(x) == 1}
    return dup