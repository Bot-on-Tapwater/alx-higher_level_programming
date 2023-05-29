#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            try:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end="")
                    count += 1
            except IndexError:
                break
    except TypeError:
        raise Exception("An exception occurred: x is larger than the length of my_list")
    finally:
        print()
        return count
