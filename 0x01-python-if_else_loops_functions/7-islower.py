#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        # print("{}".format(chr(i)), end='')
        if (c == chr(i)):
            return True
    return False
