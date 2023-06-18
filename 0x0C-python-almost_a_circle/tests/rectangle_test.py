#!/usr/bin/python3

"""
Unittests for Class Rectangle
"""
import unittest
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):
    def setUp(self):
        # print("\tCreate Rectangle object my_rect")
        self.my_rect = Rectangle(10, 15, 20, 25, 120)
    
    def tearDown(self):
        pass
        # print("Finished running tests")
    
    """
    Test cases associated with creating instance
    """
    def test_create_instance(self):
        self.assertIsInstance(Rectangle(1, 2), Rectangle)

    def test_create_instance_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
    
    def test_create_instance_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_create_instance_negatives_dims(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, -2)
    
    def test_create_instance_negatives_offs(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1, -2)

    def test_create_instance_zero_dims(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 0)

    def test_create_instance_nonints_dims(self):
        with self.assertRaises(TypeError):
            Rectangle([1, 2], [1, 3, 5])
    
    def test_create_instance_nonints_offs(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "one", "two")

    # def test_create_instance_nonints_id(self):
    #     with self.assertRaises(TypeError):
    #         Rectangle(1, 2, 3, 4, "five")

    def test_create_instance_excess_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)
    
    """
    Test cases associated with setters and getters
    """
    def test_set_attr_width(self):
        self.my_rect.width = 121
        self.assertEqual(self.my_rect.width, 121)

    def test_set_attr_height(self):
        self.my_rect.height = 1738
        self.assertEqual(self.my_rect.height, 1738)

    def test_set_attr_x(self):
        self.my_rect.x = 10
        self.assertEqual(self.my_rect.x, 10)

    def test_set_attr_y(self):
        self.my_rect.y = 15
        self.assertEqual(self.my_rect.y, 15)

    def test_set_attr_id(self):
        self.my_rect.id = 99
        self.assertEqual(self.my_rect.id, 99)

    def test_set_attr_width_zero(self):
        with self.assertRaises(ValueError):
            self.my_rect.width = 0

    def test_set_attr_height_zero(self):
        with self.assertRaises(ValueError):
            self.my_rect.height = 0

    def test_set_attr_x_negative(self):
        with self.assertRaises(ValueError):
            self.my_rect.x = -10

    def test_set_attr_y_negative(self):
        with self.assertRaises(ValueError):
            self.my_rect.y = -15

    def test_set_attr_width_negative(self):
        with self.assertRaises(ValueError):
            self.my_rect.width = -5

    def test_set_attr_height_negative(self):
        with self.assertRaises(ValueError):
            self.my_rect.height = -5

    def test_set_attr_x_nonints(self):
        with self.assertRaises(TypeError):
            self.my_rect.x = "String"

    def test_set_attr_y_nonints(self):
        with self.assertRaises(TypeError):
            self.my_rect.y = [11]

    def test_set_attr_width_nonints(self):
        with self.assertRaises(TypeError):
            self.my_rect.width = {}

    def test_set_attr_height_nonints(self):
        with self.assertRaises(TypeError):
            self.my_rect.height = (1,)

if __name__ == '__main__':
    unittest.main()