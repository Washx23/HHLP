#!/usr/bin/python3
import sys 
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("{} argument:".format(len(sys.argv)-1))
    elif len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv)-1))       
    else:
        print("{} arguments:".format(len(sys.argv)-1))
        for args in range(len(sys.argv)):
            count = int(args)
            if count != 0:
                print("{}: {}".format(count, str(sys.argv[args])))
