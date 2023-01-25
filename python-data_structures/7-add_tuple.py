#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    
    while len(tuple_b) < 2:
        apl = list(tuple_b)
        apl.append(0)
        p = tuple(apl)
        recu = add_tuple(tuple_a, p)
        return recu
    while len(tuple_a) < 2:
        apl = list(tuple_a)
        apl.append(0)
        p = tuple(apl)
        recu = add_tuple(tuple_b, p)
        return recu
    if len(tuple_b) > 2 and len(tuple_a) > 2:
        apl = list(tuple_b)
        cp = list(tuple_a)
        apl = tuple(apl[:2])
        cp = tuple(cp[:2])
        recu = add_tuple(apl, cp)
        return recu
    new_tuple = tuple([a + b for a, b in (zip(tuple_a, tuple_b))])    
    return new_tuple
