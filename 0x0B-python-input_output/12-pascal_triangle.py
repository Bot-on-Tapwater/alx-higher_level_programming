#!/usr/bin/python3

"""
Pascal's triangle
"""


def pascal_triangle(n):
    """
    Pascal's triangle
    """
    pascal_list = []
    small_list = []
    list_size = 1
    default_integer = 1
    temp_list = []

    for i in range(n):
        # print(f"Loop {i}")
        for j in range(list_size):
            # print(f"\tInserting at index: {j} to small list")
            if (default_integer == 1):
                # print(f"\t\tAdding {default_integer} to small list")
                small_list.append(default_integer)
                default_integer = 0
            else:
                num1 = 0
                num2 = 0
                try:
                    num1 = temp_list[j]
                except IndexError:
                    num1 = 0
                try:
                    num2 = temp_list[j - 1]
                except IndexError:
                    num2 = 0
                small_list.append(num1 + num2)

        # print(f"\t\t\tCurrent small_list:{small_list}")
        pascal_list.append(small_list)

        temp_list = small_list[:]
        # print(f"\t\t\tCurrent temp_list:{small_list}")
        small_list = []
        default_integer = 1
        list_size += 1

    return pascal_list
