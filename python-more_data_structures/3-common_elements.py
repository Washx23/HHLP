#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = list(set_1) + list(set_2)
    prot = set()
    return [x for x in new_list if x in prot or (prot.add(x) or False)]
