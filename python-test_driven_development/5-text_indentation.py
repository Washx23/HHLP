#!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of these characters: ., ? and :
"""

def text_indentation(text):
    """ function"""
    if type(text)==str:
        text = text.replace("?", "?\n\n")
        text = text.replace(".", ".\n\n")
        text = text.replace(":", ":\n\n")
        text = text.replace("\n ", "\n")
        print(text)
