#!/usr/bin/python3

def text_indentation(text):
    if type(text)==str:
        text = text.replace("?", "?\n\n")
        text = text.replace(".", ".\n\n")
        text = text.replace(":", ":\n\n")
        text = text.replace("\n ", "\n")
        print(text)
