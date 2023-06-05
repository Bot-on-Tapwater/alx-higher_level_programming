#!/usr/bin/python3
""" Create class: Rectangle """


class Rectangle:
    """Empty class Rectangle"""
    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle.

        Args:
            __width(int): Width of rectangle
            __height(int): Height of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """ Getter for height """
        return (self.__height)

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ Getter for width """
        return (self.__width)

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
