#!/usr/bin/python3

import pep8
import inspect
import unittest
from models.base import Base
from models.rectangle import Rectangle
from contextlib import contextmanager
import json
import sys
from io import StringIO


class TestRectangleClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        Base._Base__nb_objects = 0
        cls.test = Rectangle(10, 2)
        cls.test1 = Rectangle(1, 2, 5, 5)
        cls.test2 = Rectangle(5, 9, 8, 7, 9)
        cls.test3 = Rectangle(3, 8, 3, 4)
        cls.all_functions = inspect.getmembers(Rectangle, inspect.isfunction)

    def setup(self):

        r1 = r2 = temp = temp1 = output = 0

    def test_pep8_model(self):

        style = pep8.StyleGuide(quiet=True)
        pepp = style.check_files(['models/rectangle.py'])
        self.assertEqual(pepp.total_errors, 0, "fix pep8")

    def test_pep8_test(self):

        style = pep8.StyleGuide(quiet=True)
        pepp = style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(pepp.total_errors, 0, "fix pep8")

    def test_doctest(self):

        self.assertTrue(Rectangle.__doc__)
        for i in self.all_functions:
            self.assertTrue(i[1].__doc__)

    def test_class(self):

        self.assertTrue(isinstance(self.test, Rectangle))

    def test_class_inheritance(self):

        self.assertTrue(issubclass(type(self.test), Base))

    def test_class_init(self):

        self.assertEqual(self.test.id, 1)
        self.assertEqual(self.test1.id, 2)
        self.assertEqual(self.test2.id, 9)
        self.assertEqual(self.test3.id, 3)

    def test_class_variables(self):

        self.assertEqual(self.test.width, 10)
        self.assertEqual(self.test1.width, 1)
        self.assertEqual(self.test2.width, 5)
        self.assertEqual(self.test3.width, 3)
        self.assertEqual(self.test.height, 2)
        self.assertEqual(self.test1.height, 2)
        self.assertEqual(self.test2.height, 9)
        self.assertEqual(self.test3.height, 8)
        self.assertEqual(self.test1.x, 5)
        self.assertEqual(self.test2.x, 8)
        self.assertEqual(self.test3.x, 3)
        self.assertEqual(self.test1.y, 5)
        self.assertEqual(self.test2.y, 7)
        self.assertEqual(self.test3.y, 4)

    def test_input_errors(self):

        self.assertRaises(TypeError, Rectangle, ())
        self.assertRaises(TypeError, Rectangle, (1))

    def test_integer_validator(self):

        with self.assertRaises(TypeError, msg="width must be an integer"):
            temp = Rectangle("a", "b")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            temp = Rectangle(1, "b")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            temp = Rectangle(1, 1, "a", 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            temp = Rectangle(1, 2, 4, "a")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            temp = Rectangle(-1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            temp = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            temp = Rectangle(1, 1, -1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            temp = Rectangle(1, 2, 0, -1)

    def test_area(self):

        self.assertEqual(self.test.area(), 20)
        self.assertEqual(self.test1.area(), 2)
        self.assertEqual(self.test2.area(), 45)
        self.assertEqual(self.test3.area(), 24)
        with self.assertRaises(TypeError):
            r = self.test.area(2)

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
            temp = Rectangle(2, 2)
            temp.display()
            output = out.getvalue().strip()
            self.assertEqual(output, "##\n##")

        with test_display() as out:
            temp = Rectangle(2, 2, 2, 2)
            temp.display()
            output = out.getvalue()
            self.assertEqual(output, "\n\n  ##\n  ##\n")

    def test_str(self):

        self.assertEqual(str(self.test), "[Rectangle] (1) 0/0 - 10/2")
        self.assertEqual(str(self.test1), "[Rectangle] (2) 5/5 - 1/2")
        self.assertEqual(str(self.test2), "[Rectangle] (9) 8/7 - 5/9")
        self.assertEqual(str(self.test3), "[Rectangle] (3) 3/4 - 3/8")

    def test_update_0(self):

        temp = Rectangle(5, 6)
        self.assertEqual(temp.width, 5)
        self.assertEqual(temp.height, 6)
        temp.update(3, 4)
        self.assertEqual(temp.id, 3)
        self.assertEqual(temp.width, 4)
        temp.update(9, 8, 7, 6, 5)
        self.assertEqual(temp.id, 9)
        self.assertEqual(temp.width, 8)
        self.assertEqual(temp.height, 7)
        self.assertEqual(temp.x, 6)
        self.assertEqual(temp.y, 5)

    def test_update_1(self):

        temp = Rectangle(9, 8, 7, 6, 5)
        self.assertEqual(str(temp), "[Rectangle] (5) 7/6 - 9/8")
        temp.update(id=1)
        self.assertEqual(temp.id, 1)
        temp.update(height=2)
        self.assertEqual(temp.height, 2)
        temp.update(width=3)
        self.assertEqual(temp.width, 3)
        temp.update(x=4)
        self.assertEqual(temp.x, 4)
        temp.update(y=12)
        self.assertEqual(temp.y, 12)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            temp.update(1, "a")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            temp.update(1, 1, "a")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            temp.update(1, 1, 1, "a")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            temp.update(1, 1, 1, 1, "a")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            temp.update(1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            temp.update(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            temp.update(1, 1, 1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            temp.update(1, 1, 1, 1, -2)
        temp.update(2, 1, 1, 1, 1, 2)
        self.assertEqual(str(temp), "[Rectangle] (2) 1/1 - 1/1")
        temp.update()
        self.assertEqual(str(temp), "[Rectangle] (2) 1/1 - 1/1")

    def test_to_dictionary(self):

        temp = Rectangle(10, 21, 1, 9, 5)
        r1 = temp.to_dictionary()
        r2 = {'x': 1, 'y': 9, 'id': 5, 'height': 21, 'width': 10}
        self.assertEqual(r1, r2)
        self.assertTrue(type(r1) is dict)

    def test_to_json_string(self):

        temp = Rectangle(10, 7, 2, 8, 1)
        r1 = temp.to_dictionary()
        r2 = temp.to_json_string(r1)
        self.assertEqual(r2, json.dumps(r1))

    def test_json_string_to_file(self):

        temp1 = Rectangle(5, 6, 2, 9, 4)
        temp2 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([temp1, temp2])
        with open("Rectangle.json") as file:
            r1 = file.read()
            r2 = [temp1.to_dictionary(), temp2.to_dictionary()]
            self.assertEqual(json.dumps(r2), r1)

    def test_from_json(self):

        temp1 = Rectangle(5, 6, 2, 9, 4)
        temp2 = Rectangle(1, 2, 3, 4, 5)
        r1 = [temp1.to_dictionary(), temp2.to_dictionary()]
        self.assertTrue(isinstance(r1, list))
        r2 = Rectangle.to_json_string(r1)
        self.assertTrue(isinstance(r2, str))
        r3 = Rectangle.from_json_string(r2)
        self.assertTrue(isinstance(r3, list))

    def test_create(self):

        r1 = Rectangle(4, 8, 9)
        dict1 = r1.to_dictionary()
        r2 = Rectangle.create(**dict1)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):

        r1 = Rectangle(1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2)
        lists = [r1, r2]
        Rectangle.save_to_file(lists)
        output = Rectangle.load_from_file()
        self.assertTrue(isinstance(output, list))
        o1 = output[0]
        o2 = output[1]
        self.assertTrue(isinstance(o1, Rectangle))
        self.assertTrue(isinstance(o2, Rectangle))
        self.assertEqual(str(r1), str(o1))
        self.assertEqual(str(r2), str(o2))

    def test_return_empty(self):

        output = Rectangle.to_json_string(None)
        self.assertEqual(output, "[]")
        output = Rectangle.to_json_string([])
        self.assertEqual(output, "[]")

    def test_save_empty(self):

        lists = []
        Rectangle.save_to_file(lists)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_None(self):

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_load_no_file(self):

        try:
            Rectangle.save_to_file(None)
            os.remove("Rectangle.json")
        except BaseException:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_empty_file(self):

        try:
            Rectangle.save_to_file(None)
            os.remove("Rectangle.json")
        except BaseException:
            pass
        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_csv(self):

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_input = [r1, r2]

        Rectangle.save_to_file_csv(list_input)

        list_output = Rectangle.load_from_file_csv()

        o1 = list_output[0]
        o2 = list_output[1]
        self.assertTrue(isinstance(o1, Rectangle))
        self.assertTrue(isinstance(o2, Rectangle))
        self.assertEqual(str(r1), str(o1))
        self.assertEqual(str(r2), str(o2))

    def test_no_csv(self):

        try:
            Rectangle.save_to_file_csv(None)
            os.remove("Rectangle.json")
        except BaseException:
            pass
        self.assertEqual(Rectangle.load_from_file_csv(), [])

    def test_load_empty_csv(self):

        try:
            Rectangle.save_to_file_csv(None)
            os.remove("Rectangle.json")
        except BaseException:
            pass
        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file_csv(), [])
