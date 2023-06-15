#!/usr/bin/python3

"""
Creates class Base
"""


class Base:
    """
    class Base

    args:
        def __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method
        """
        # self.id = id
        if (id is not None):
            self.id = id
        else:
            # use type(self) since __nb_objects is private attr
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
