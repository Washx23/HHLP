#!/usr/bin/python3
import sys 
if __name__ == '__main__':
    print("{} arguments:".format(len(sys.argv)-1))
    for args in range(len(sys.argv)):
        count = int(args)
        if count != 0:
            print("{}: {}".format(count, str(sys.argv[args])))
