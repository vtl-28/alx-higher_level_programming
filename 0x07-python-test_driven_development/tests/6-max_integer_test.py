#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""

    def test_module_docstring(self):
        """Tests for module docsting"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_type(self):
        self.assertIsInstance([1, 2, 3, 4], list)

    def test_if_empty(self):
        self.assertIsNone(max_integer([]))
    
    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)



if __name__ == "__main__":
    unittest.main()
