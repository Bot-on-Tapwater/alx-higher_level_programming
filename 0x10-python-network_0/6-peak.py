#!/usr/bin/python3
"""Find peak in a list of integers"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (List[int]): List of unsorted integers.

    Returns:
        int or None: The peak element if found, or None if the list is empty.

    Complexity:
        O(log(n))
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
