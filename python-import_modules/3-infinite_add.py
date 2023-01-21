#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    b = 0
    for a in range(1, len(argv)):
        b += int(argv[a])
    print("{}".format(b))
