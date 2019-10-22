k!/usr/bin/python3

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):



    def test_id_valid(self):

        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_valid_multiple(self):

        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base()
        self.assertEqual(b3.id, 4)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 5)

    def test_id_valid_same_id(self):

        b6 = Base(77)
        self.assertEqual(b6.id, 77)
        b7 = Base(77)
        self.assertEqual(b7.id, 77)

    def test_id_valid_param_str(self):

        b8 = Base("Holberton")
        self.assertEqual(b8.id, "Holberton")

    def test_id_valid_param_list(self):

        b9 = Base([98, 977])
        self.assertEqual(b9.id, [98, 977])

    def test_id_valid_param_tuple(self):

        b10 = Base((98, 977))
        self.assertEqual(b10.id, (98, 977))

    def test_id_valid_param_dict(self):

        b11 = Base({"98": 977})
        self.assertEqual(b11.id, {"98": 977})

    def test_id_valid_param_set(self):

        b12 = Base({"98", 977})
        self.assertEqual(b12.id, {"98", 977})

    def test_id_valid_param_float(self):

        b13 = Base(3.14)
        self.assertEqual(b13.id, 3.14)

    def test_id_valid_param_inf(self):

        b14 = Base(float('inf'))
        self.assertEqual(b14.id, float('inf'))

    def test_id_valid_param_func(self):

        b15 = Base(len)
        self.assertEqual(b15.id("Hi"), 2)

    def test_id_valid_isprivate(self):

        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_params_exceptions_args_six(self):

        with self.assertRaises(TypeError):
            r = Base(2, 3, 23, 12, 234, 4)

if __name__ == '__main__':
    unittest.main()
