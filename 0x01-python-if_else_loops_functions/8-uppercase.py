#!/usr/bin/python3
def uppercase(str):
    modified_string = ""
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            modified_char = chr(ord(c) - 32)
            modified_string += modified_char
        else:
            modified_string += c
    print("{}".format(modified_string))
