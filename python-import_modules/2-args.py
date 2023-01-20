#!/usr/bin/python3
import sys 
if __name__ == '__main__':
    count = len(sys.argv)
    if count == 1:
        print("0 arguments.")
    elif count == 2:
        print("1 argument:")
        for args in range(1, len(sys.argv)):
            p = int(args)
            print("{}: {}".format(p, str(sys.argv[args])))
    else:
        print("{} arguments:".format(count - 1))
        for args in range(1, len(sys.argv)):
            p = int(args)
            print("{}: {}".format(p, str(sys.argv[args])))
