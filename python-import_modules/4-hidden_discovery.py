#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    txt = dir(hidden_4)
    for a in txt:
        if not a.startswith("__"):
            print("{}".format(a))
