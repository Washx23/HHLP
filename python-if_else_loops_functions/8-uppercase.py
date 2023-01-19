#!/usr/bin/python3
def uppercase(str):
    newtext = ""
    for a in str:
        if ord(a) > 96 and ord(a) < 123:
            newtext += chr(ord(a)-32)
        else:
            newtext += a
    print(newtext)