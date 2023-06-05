#!/usr/bin/python3
""" Create class: Rectangle """


class Rectangle:
    """Empty class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle.

        Args:
            __width(int): Width of rectangle
            __height(int): Height of rectangle
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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

    def area(self):
        """Calculates area of a rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """Calculates perimeter of a rectangle"""
        if (self.height == 0 or self.width == 0):
            return (0)
        else:
            return ((self.height + self.width) * 2)

    def __str__(self):
        """Prints rectangle using # shapes"""
        my_list = ""
        if (self.width == 0 or self.height == 0):
            return ("")
        else:
            for j in range(self.height):
                for i in range(self.width):
                    my_list += str(self.print_symbol)
                if (j < self.height - 1):
                    my_list += "\n"
            return (my_list)

    def __repr__(self):
        """Prints string representation"""
        num1 = str(self.width)
        num2 = str(self.height)
        return "Rectangle(" + num1 + ", " + num2 + ")"

    def __del__(self):
        """Prints string before deleting instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a square instance
        
        Args:
            size (int): Size of the square
        """
        return cls(size, size)
