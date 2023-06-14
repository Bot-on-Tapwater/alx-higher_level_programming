#!/usr/bin/python3

"""
create class MyInt
"""


class MyInt(int):
    """
    create class MyInt
    """
    def __eq__(self, other):
        """magic function"""
        return super().__ne__(other)

    def __ne__(self, other):
        """magic function"""
        return super().__eq__(other)
