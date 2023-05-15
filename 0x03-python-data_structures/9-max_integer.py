#!/usr/bin/python3


def max_integer(my_list=[]):
    max_int = 0

    for integer in my_list:
        if (max_int < integer):
            max_int = integer
        else:
            continue

    return max_int
