#!/usr/bin/python3

"""
Unittests for Class Rectangle
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import os


class Test_Rectangle(unittest.TestCase):
    def setUp(self):
        # print("\tCreate Rectangle object my_rect")
        self.my_rect = Rectangle(10, 15, 20, 25, 120)
        self.small_rect = Rectangle(2, 2, 2, 2)
        self.my_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.file_name = "Rectangle.json"

        if os.path.exists(self.file_name):
            os.remove(self.file_name)

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

    """
    Cases associated with area() method
    """
    def test_area(self):
        self.assertEqual(self.my_rect.area(), 150)

    def test_area_with_args(self):
        with self.assertRaises(TypeError):
            self.my_rect.area(10)

    """
    Cases associated with display() method
    """
    def test_display(self):
        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function
        self.small_rect.display()

        # Get the value of the printed output
        printed_output = captured_output.getvalue().strip()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Assert on the expected output
        expected_output = '\n  ##\n  ##\n'.strip()
        self.assertEqual(printed_output, expected_output)

    def test_display_with_args(self):
        with self.assertRaises(TypeError):
            self.my_rect.display(10, 43)

    """
    Cases associated with __str__()
    """
    def test_str(self):
        self.assertEqual(str(self.my_rect), "[Rectangle] (120) 20/25 - 10/15")

    """
    Cases associated with update()
    """
    def test_update_no_args(self):
        self.my_rect.update()
        self.assertEqual(str(self.my_rect), "[Rectangle] (120) 20/25 - 10/15")

    def test_update_args(self):
        self.my_rect.update(66, 77, 88, 99, 55)
        self.assertEqual(str(self.my_rect), "[Rectangle] (66) 99/55 - 77/88")

    def test_update_kwargs(self):
        self.my_rect.update(x=27, y=19)
        self.assertEqual(str(self.my_rect), "[Rectangle] (120) 27/19 - 10/15")

    def test_update_args_and_kwargs(self):
        self.my_rect.update(65, x=27, y=19)
        self.assertEqual(str(self.my_rect), "[Rectangle] (65) 20/25 - 10/15")

    def test_update_kwargs_nonattrs(self):
        self.my_rect.update(z=27, q=19)
        self.assertEqual(str(self.my_rect), "[Rectangle] (120) 20/25 - 10/15")

    def test_update_excess_args(self):
        """To be looked into"""
        self.my_rect.update(66, 77, 88, 99, 55, 44, 22, 11, 33)
        self.assertEqual(str(self.my_rect), "[Rectangle] (66) 99/55 - 77/88")

    def test_update_args_nonints_args(self):
        with self.assertRaises(TypeError):
            self.my_rect.update("k", "j", "ls")

    def test_update_dims_negative_args(self):
        with self.assertRaises(ValueError):
            self.my_rect.update(1, -1, -2)

    def test_update_dims_zero_args(self):
        with self.assertRaises(ValueError):
            self.my_rect.update(1, 0, 0)

    def test_update_offs_negative_args(self):
        with self.assertRaises(ValueError):
            self.my_rect.update(1, 1, 1, -2, -2)

    def test_update_args_nonints_kwargs(self):
        with self.assertRaises(TypeError):
            self.my_rect.update(x=27, y=19, height=[1], width=[2])

    def test_update_dims_negative_kwargs(self):
        with self.assertRaises(ValueError):
            self.my_rect.update(x=27, y=19, height=-1, width=-2)

    def test_update_dims_zero_kwargs(self):
        with self.assertRaises(ValueError):
            self.my_rect.update(x=27, y=19, height=0, width=0)

    def test_update_offs_negative_kwargs(self):
        with self.assertRaises(ValueError):
            self.my_rect.update(x=-27, y=-19, height=1, width=1)

    """
    Cases associated with to_dictionary()
    """
    def test_to_dictionary(self):
        self.assertIsInstance(self.my_rect.to_dictionary(), dict)

    def test_to_dictionary_attrs_prsnt(self):
        self.assertIn("width", self.my_rect.to_dictionary())
        self.assertIn("height", self.my_rect.to_dictionary())
        self.assertIn("x", self.my_rect.to_dictionary())
        self.assertIn("y", self.my_rect.to_dictionary())
        self.assertIn("id", self.my_rect.to_dictionary())

        # self.my_rect = Rectangle(10, 15, 20, 25, 120)
        self.assertEqual(self.my_rect.x, self.my_rect.to_dictionary()["x"])
        self.assertEqual(self.my_rect.y, self.my_rect.to_dictionary()["y"])
        self.assertEqual(self.my_rect.id, self.my_rect.to_dictionary()["id"])

    def test_to_dictionary_with_args(self):
        with self.assertRaises(TypeError):
            self.my_rect.to_dictionary("string")

    """
    Cases associated with to_json_string
    """
    def test_to_json_string(self):
        self.assertIsInstance(self.my_rect.to_json_string(self.my_dict), str)

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            self.my_rect.to_json_string()

    def test_to_json_string_nondict(self):
        self.assertIsInstance(self.my_rect.to_json_string([1, 2, 3]), str)

    """
    Cases associated with save_to_file()
    """
    def test_save_to_file(self):
        self.my_rect.save_to_file([self.my_rect, self.small_rect])
        self.assertTrue(os.path.exists(self.file_name))


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 2)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 2)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Python')

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b'abcdefg'))

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'abcedfg'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittests for testing Rectangle order of attribute initialization."""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def test_area_small(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_area_large(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_area_changed_attributes(self):
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test __str__ method
    def test_str_method_print_width_height(self):
        r = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # Test display method
    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Rectangle class."""

    # Test args
    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == '__main__':
    unittest.main()
