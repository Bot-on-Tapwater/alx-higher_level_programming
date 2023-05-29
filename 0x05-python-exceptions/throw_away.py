#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0

        for elem in my_list:
            if (count < x):
                print("{}".format(elem), end="")
                count += 1
            else:
                print()
                return (my_list)
    
    except TypeError:
        print("Type unsupported")