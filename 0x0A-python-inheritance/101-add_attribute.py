#!/usr/bin/python3
"""
add attributes to an object
"""


def add_attribute(obj, attribute_name, attribute_value):
    """
    adds attributes to an object
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute_name, attribute_value)
