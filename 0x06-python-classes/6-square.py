#!/usr/bin/python3
# 0-square.py
# Munda Brandon <mundabrandon@outlook.com>
"""Define a class Square with size attribute"""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
            position (tuple): Location of a point.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter for size attribute """
        return self.__size

    @size.setter
    def size(self, size):
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """Getter for position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(value[0], int) or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(value[1], int) or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square to stdout"""
        if (self.__size == 0):
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size, end="")
                print()
