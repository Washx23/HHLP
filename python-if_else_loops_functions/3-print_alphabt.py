#!/usr/bin/python3
for i in range(26):
    alp = chr(ord('a') + i)
    if alp != 'e' and alp != 'q':
        print("{}".format(alp), end="")
