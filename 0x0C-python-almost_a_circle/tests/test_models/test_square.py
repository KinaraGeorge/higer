#!/usr/bin/python3

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from contextlib import contextmanager
import json
import sys
import os
from io import StringIO


class TestSquareClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        Base._Base__nb_objects = 0
        cls.test = Square(10)
        cls.test1 = Square(1, 2, 5)
        cls.test2 = Square(5, 9, 8, 9)
        cls.test3 = Square(3, 8, 3, 4)

    def setUp(self):

        r1 = r2 = output = temp = 0

    def test_doctest(self):

        self.assertIsNotNone(Base.__doc__)

    def test_class(self):

        self.assertTrue(isinstance(self.test, Square))

    def test_class_inheritance(self):

        self.assertTrue(issubclass(type(self.test), Base))

    def test_pep8_model(self):

        style = pep8.StyleGuide(quiet=True)
        pepp = style.check_files(['models/square.py'])
        self.assertEqual(pepp.total_errors, 0, "fix pep8")

    def test_pep8_test(self):

        style = pep8.StyleGuide(quiet=True)
        pepp = style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(pepp.total_errors, 0, "fix pep8")

    def test_class_init(self):

        self.assertEqual(self.test.id, 1)
        self.assertEqual(self.test1.id, 2)
        self.assertEqual(self.test2.id, 9)
        self.assertEqual(self.test3.id, 4)

    def test_class_variables(self):

        self.assertEqual(self.test.size, 10)
        self.assertEqual(self.test1.size, 1)
        self.assertEqual(self.test2.size, 5)
        self.assertEqual(self.test3.size, 3)
        self.assertEqual(self.test1.x, 2)
        self.assertEqual(self.test2.x, 9)
        self.assertEqual(self.test3.x, 8)
        self.assertEqual(self.test1.y, 5)
        self.assertEqual(self.test2.y, 8)
        self.assertEqual(self.test3.y, 3)

    def test_input_errors(self):

        self.assertRaises(TypeError, Square, ())

    def test_integer_validator(self):

        with self.assertRaises(TypeError, msg="width must be an integer"):
            temp = Square("a", "b")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            temp = Square(1, "b")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            temp = Square(1, 1, "b")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            temp = Square(-1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            temp = Square(1, -1, -1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            temp = Square(1, 2, -1, -1)

    def test_area(self):

        self.assertEqual(self.test.area(), 100)
        self.assertEqual(self.test1.area(), 1)
        self.assertEqual(self.test2.area(), 25)
        self.assertEqual(self.test3.area(), 9)

    def test_display_0_1(self):

        @contextmanager
        def test_display():
            new_out = old_out = ""
            new_out = StringIO()
            old_out = sys.stdout
            try:
                sys.stdout = new_out
                yield sys.stdout
            finally:
                sys.stdout = old_out
        with test_display() as out:
            temp = Square(3)
            temp.display()
            output = out.getvalue().strip()
            self.assertEqual(output, "###\n###\n###")

        with test_display() as out:
            temp = Square(3, 2, 2)
            temp.display()
            output = out.getvalue()
            self.assertEqual(output, "\n\n  ###\n  ###\n  ###\n")

    def test_str(self):

        self.assertEqual(str(self.test), "[Square] (1) 0/0 - 10")
        self.assertEqual(str(self.test1), "[Square] (2) 2/5 - 1")
        self.assertEqual(str(self.test2), "[Square] (9) 9/8 - 5")
        self.assertEqual(str(self.test3), "[Square] (4) 8/3 - 3")

    def test_update_0(self):

        temp = Square(5)
        self.assertEqual(temp.size, 5)
        temp.update(3, 4)
        self.assertEqual(temp.id, 3)
        self.assertEqual(temp.size, 4)
        temp.update(9, 8, 7, 6)
        self.assertEqual(temp.id, 9)
        self.assertEqual(temp.size, 8)
        self.assertEqual(temp.x, 7)
        self.assertEqual(temp.y, 6)

    def test_update_1(self):

        temp = Square(9, 8, 7, 6)
        self.assertEqual(str(temp), "[Square] (6) 8/7 - 9")
        temp.update(id=1)
        self.assertEqual(temp.id, 1)
        temp.update(size=3)
        self.assertEqual(temp.size, 3)
        temp.update(x=4)
        self.assertEqual(temp.x, 4)
        temp.update(y=12)
        self.assertEqual(temp.y, 12)

    def test_getter_setter(self):

        temp = Square(5)
        self.assertEqual(temp.size, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            temp.size = "9"

    def test_to_dictionary(self):

        temp = Square(10, 2, 1, 9)
        r1 = temp.to_dictionary()
        self.assertEqual(r1, {'id': 9, 'x': 2, 'size': 10, 'y': 1})

    def test_to_json_string(self):

        temp = Square(10, 2, 1, 9)
        s1 = temp.to_dictionary()
        s2 = temp.to_json_string(s1)
        self.assertEqual(s2, json.dumps(s1))

    def test_json_string_to_file(self):

        temp1 = Square(5, 6, 2, 9)
        temp2 = Square(1, 2, 3, 4)
        Square.save_to_file([temp1, temp2])
        with open("Square.json") as file:
            r1 = file.read()
            r2 = [temp1.to_dictionary(), temp2.to_dictionary()]
            self.assertEqual(json.dumps(r2), r1)

    def test_from_json(self):

        temp1 = Square(5, 6, 2, 9)
        temp2 = Square(1, 2, 3, 4)
        r1 = [temp1.to_dictionary(), temp2.to_dictionary()]
        self.assertTrue(isinstance(r1, list))
        r2 = Square.to_json_string(r1)
        self.assertTrue(isinstance(r2, str))
        r3 = Square.from_json_string(r2)
        self.assertTrue(isinstance(r3, list))

    def test_create(self):

        r1 = Square(4, 8, 9)
        dict1 = r1.to_dictionary()
        r2 = Square.create(**dict1)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):

        r1 = Square(1, 1, 1)
        r2 = Square(2, 2, 2)
        lists = [r1, r2]
        Square.save_to_file(lists)
        output = Square.load_from_file()
        self.assertTrue(isinstance(output, list))
        o1 = output[0]
        o2 = output[1]
        self.assertTrue(isinstance(o1, Square))
        self.assertTrue(isinstance(o2, Square))
        self.assertEqual(str(r1), str(o1))
        self.assertEqual(str(r2), str(o2))

    def test_return_empty(self):

        output = Square.to_json_string(None)
        self.assertEqual(output, "[]")
        output = Square.to_json_string([])
        self.assertEqual(output, "[]")

    def test_save_empty(self):

        lists = []
        Square.save_to_file(lists)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_None(self):

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_load_no_file(self):

        try:
            Square.save_to_file(None)
            os.remove("Square.json")
        except BaseException:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_load_empty_file(self):

        try:
            Square.save_to_file(None)
            os.remove("Square.json")
        except BaseException:
            pass
        open("Square.json", 'a').close()
        self.assertEqual(Square.load_from_file(), [])

    def test_csv(self):

        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        list_input = [r1, r2]

        Square.save_to_file_csv(list_input)

        list_output = Square.load_from_file_csv()

        o1 = list_output[0]
        o2 = list_output[1]
        self.assertTrue(isinstance(o1, Square))
        self.assertTrue(isinstance(o2, Square))
        self.assertEqual(str(r1), str(o1))
        self.assertEqual(str(r2), str(o2))

    def test_no_csv(self):

        try:
            Square.save_to_file_csv(None)
            os.remove("Square.json")
        except BaseException:
            pass
        self.assertEqual(Square.load_from_file_csv(), [])

    def test_load_empty_csv(self):

        try:
            Square.save_to_file_csv(None)
            os.remove("Square.json")
        except BaseException:
            pass
        open("Square.json", 'a').close()
        self.assertEqual(Square.load_from_file_csv(), [])
