#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([10]), 10)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_float_list(self):
        self.assertAlmostEqual(max_integer([1.5, 2.8, 3.2]), 3.2)
        self.assertAlmostEqual(max_integer([-1.1, -2.2, -3.3], -1.1))
        self.assertAlmostEqual(max_integer([0.5, 0.3, 0.7]), 0.7)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)

    def test_mixed_integer_types(self):
        self.assertEqual(max_integer([1, 2, 3, 2.5]), 3)
        self.assertEqual(max_integer([1.5, 2, 3, 2]), 3)
        self.assertEqual(max_integer([-1, -2, -3, 2.5]), -1)
        self.assertEqual(max_integer([-1.5, -2, -3, -2]), -1)


if __name__ == '__main__':
    unittest.main()
