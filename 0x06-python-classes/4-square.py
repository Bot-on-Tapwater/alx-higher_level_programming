#!/usr/bin/python3
# 0-square.py
# Munda Brandon <mundabrandon@outlook.com>
"""Define a class Square with size attribute"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    """Getter for size attribute """
    def size(self):
        return self.__size

    @size.setter
    """Setter for size attribute"""
    def size(self, size):
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
