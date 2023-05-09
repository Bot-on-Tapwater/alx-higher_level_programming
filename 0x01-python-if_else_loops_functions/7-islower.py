#!/usr/bin/python3
def islower(c):
    # if (ord(c) >= 97 and ord(c) <= 122):
    #     return True
    # else:
    #     return False
    for i in range(97, 123):
        if (ord(c) == i):
            return True
    return False
