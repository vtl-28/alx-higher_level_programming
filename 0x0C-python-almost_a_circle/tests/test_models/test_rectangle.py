#!/usr/bin/python3
""" Module for test Rectangle class """

import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """ Suite to test Rectangle class """

    def test_no_id1(self):
        ''' test with no id '''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_no_id2(self):
        ''' test wit no id '''
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

    def test_with_id(self):
        ''' test with id '''
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_height_type(self):
        ''' check height type '''
        with self.assertRaises(TypeError, msg="height must be an integer"):
            new = Rectangle(10, "2")

    def test_width_value(self):
        ''' check with value '''
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r = Rectangle(10, 2)
            r.width = -10

    def test_x_type(self):
        ''' check x type '''
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r = Rectangle(10, 2)
            r.x = {}

    def test_height_value(self):
        ''' check height value '''
        with self.assertRaises(ValueError, msg="y must be > 0"):
            Rectangle(10, 2, 3, -1)

    def test_area_calc(self):
        ''' check area value '''
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_display_rect1(self):
        ''' check for display of symbols '''
        res = "####\n####\n####\n####\n####\n####\n"
        r1 = Rectangle(4, 6)
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_rect2(self):
        ''' check for display of symbols '''
        res = "##\n##\n"
        r1 = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str__1(self):
        ''' check for string rep '''
        r1 = Rectangle(4, 6, 2, 1, 12)
        res = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str__2(self):
        ''' check for string rep '''
        r2 = Rectangle(5, 5, 1)
        res = "[Rectangle] (1) 1/0 - 5/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)


if __name__ == '__main__':
    unittest.main()
