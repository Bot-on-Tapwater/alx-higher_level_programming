#!/usr/bin/python3
"""Find peak in a list of integers"""


def find_peak(list_of_integers):
    "Finds peak in a list of ints"
    if (len(list_of_integers) > 0):
        for index, value in enumerate(list_of_integers):
            try:
                lft_int = list_of_integers[(index - 1)]
            except IndexError:
                lft_int = 0

            try:
                rgt_int = list_of_integers[(index + 1)]
            except IndexError:
                rgt_int = 0

            if (value >= lft_int and value >= rgt_int):
                return value

    else:
        return None
