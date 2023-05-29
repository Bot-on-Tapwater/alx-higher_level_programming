#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = (a / b)
        specifier = ":f.1"

    except ZeroDivisionError:
        result = "None"
        specifier = ":s"

    finally:
        print("Inside result: {}".format(result))
        return (result)
