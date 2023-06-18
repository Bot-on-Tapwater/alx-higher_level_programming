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
    def test_set_attr(self):
        self.my_rect.width = 121
        self.assertEqual(self.my_rect.width, 121)

        self.my_rect.height = 1738
        self.assertEqual(self.my_rect.height, 1738)

        self.my_rect.x = 10
        self.assertEqual(self.my_rect.x, 10)

        self.my_rect.y = 15
        self.assertEqual(self.my_rect.y, 15)

        self.my_rect.id = 99
        self.assertEqual(self.my_rect.id, 99)

if __name__ == '__main__':
    unittest.main()