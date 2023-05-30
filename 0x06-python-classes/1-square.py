#!/usr/bin/python3
# 0-square.py
# Munda Brandon <mundabrandon@outlook.com>
"""Define a class Square with size attribute"""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
