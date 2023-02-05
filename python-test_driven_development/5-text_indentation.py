#!/usr/bin/python3
"""
function that prints a text
with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """ function"""
    if type(text) != str:
        raise TypeError("text must be a string")
    for iterable in "?.:":
        text = (iterable+"\n\n").join([record.strip(" ") for record in text.split(iterable)])
    print("{}".format(text), end="")
