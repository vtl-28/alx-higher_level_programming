#!/usr/bin/python3
import unittest

''' test class to test base class '''
from models.base import Base


class TestBaseClass(unittest.TestCase):
    ''' test suite '''
    def test_no_arg(self):
        ''' check for no arguments '''
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_no_arg2(self):
        ''' check for no arguments '''
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_no_arg3(self):
        ''' check for no arguments '''
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_with_arg(self):
        ''' check for arguments '''
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_no_arg4(self):
        ''' test for no arguments '''
        b5 = Base()
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
