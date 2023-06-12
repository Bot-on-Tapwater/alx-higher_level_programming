#!/usr/bin/python3
"""
Returns list of attrs and methods
"""


def lookup(obj):
    """
    returns list of attrs and methods of an obj
    """
    return [attr for attr in dir(obj)]
