#!/usr/bin/python3
""" Unit tests base """

from models.base import Base
import unittest


class Test_Base(unittest.TestCase):
    """Tests for base class."""
    def test_simple(self):

        x = Base(1)
        self.assertEqual(1, x.id)
        self.assertNotEqual(99, x.id)
        x = Base(99)
        self.assertEqual(x.id, 99)

    def test_InputErrors(self):

        with self.assertRaises(AttributeError):
            self.assertIsEqual(x(), 1)

    def test_empty(self):

        x = Base()
        self.assertEqual(1, x.id)
        x = Base(None)
        self.assertEqual(2, x.id)
        x = Base(None)
        self.assertEqual(3, x.id)
        x = Base(7)
        self.assertEqual(7, x.id)

    def test_string(self):

        x = Base(2)
        self.assertEqual(2, x.id)
        x = Base("2")
        self.assertEqual('2', x.id)

    def test_float(self):

        x = Base(3)
        self.assertEqual(3, x.id)
        x = Base(3.45)
        self.assertEqual(3.45, x.id)
        x = Base(-4.56)
        self.assertEqual(-4.56, x.id)

    def test_weird(self):

        x = Base(4)
        self.assertEqual(4, x.id)
        x = Base([1, 2])
        self.assertEqual([1, 2], x.id)
        x = Base([1, "2"])
        self.assertEqual([1, '2'], x.id)
        x = Base([1, [1, 2]])
        self.assertEqual([1, [1, 2]], x.id)
        x = Base({"perro": 2})
        self.assertEqual({"perro": 2}, x.id)
        x = Base((1, 2))
        self.assertEqual((1, 2), x.id)
        x = Base(1)
        self.assertEqual(1, x.id)
        x = Base()
        self.assertEqual(6, x.id)

    def test_more_errors(self):

        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('NaN'))
        self.assertNotEqual(float('NaN'), x.id)
        with self.assertRaises(ValueError):
            x = Base(float('bob'))
        with self.assertRaises(ValueError):
            x = Base(int('noise'))
        x = Base()
        self.assertEqual(4, x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base()
        self.assertEqual(5, x.id)

        def test_id(self):

            noise = Base()
            noiseID = noise.id
            noise2 = Base(69)
            noise3 = Base(100)
            noise4 = Base()
            self.assertTrue(noiseID, 1)
            self.assertEqual(noiseID, 1)
            self.assertFalse(noiseID, noise4.id)
            self.assertTrue(noiseID + 1, noise4.id)
            self.assertFalse(noise2, noise3)
            seld.assertEqual(noise3.id, 100)

        def test_class(self):

            noise = Base()
            self.assertTrue(issubclass(type(noise), Base))

        def test_to_json_string(self):
            pass

if __name__ == "__main__":
    unittest.main()
