#!/usr/bin/python3


import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_doctest(self):

        self.assertIsNotNone(Base.__doc__)

    def test_base_class(self):

        test = Base()
        self.assertTrue(issubclass(type(test), Base))

    def test_base_combined(self):

        initial = Base()
        one = initial.id
        initial_one = Base(75)
        two = Base()
        self.assertTrue(one + 1, two.id)

    def test_base_empty_id(self):

        b1 = Base()
        self.assertEqual(b1.id, 4)
        b2 = Base()
        self.assertEqual(b2.id, 5)
        b3 = Base()
        self.assertEqual(b3.id, 6)

    def test_base_normal(self):

        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base(2)
        self.assertEqual(b5.id, 2)


if __name__ == '__main__':
    unittest.main()
