#!/usr/bin/python3
"""
This module contains the class Base
"""
import json
import csv
import turtle
import random


class Base:
    """
    This class contains the private attribute nb objects and a constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructs id based on input
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns an input dictionary as JSON
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Reverts from json string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a JSON string to a file
        """
        strings = []
        if list_objs is not None:
            for i in list_objs:
                strings.append(cls.to_dictionary(i))
        with open(cls.__name__ + ".json", 'w') as open_file:
            open_file.write(cls.to_json_string(strings))

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of cls and returns updated values
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load information from a file and create proper class instances
        """
        lists = []
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as opened:
                lists = cls.from_json_string(opened.read())
            for i in range(len(lists)):
                lists[i] = cls.create(**lists[i])
            return lists
        except Exception:
            return lists

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save to a csv format
        """
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
            fields = ["id", "size", "x", "y"]

        with open("{}.csv".format(cls.__name__), 'w')as opened:

            if list_objs is None:
                le_writer = csv.writer(opened)
                le_writer.writerow([[]])

            else:
                le_writer = csv.DictWriter(opened, fieldnames=fields)
                le_writer.writeheader()
                for i in list_objs:
                    le_writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load data from a csv file
        """
        lists = []
        try:
            with open("{}.csv".format(cls.__name__), newline='') as opened:
                dict_reader = csv.DictReader(opened)
                for i in dict_reader:
                    for key, value in i.items():
                        i[key] = int(value)
                    dummy = cls.create(**i)
                    lists.append(dummy)
                return lists
        except Exception:
            return lists

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw shapes in rainbow
        """
        turtle.colormode(255)

        def color(x, y):
            R = random.randint(0, 256)
            G = random.randint(0, 256)
            B = random.randint(0, 256)
            turtle.pencolor(R, G, B)
            turtle.left(90)
        for i in list_rectangles:
            cnt = 0
            x = i.x
            y = i.y
            width = i.width
            height = i.height

            turtle.setpos(x, y)
            turtle.pendown()
            while cnt < 5:
                if cnt % 2 == 0:
                    turtle.fd(height)
                else:
                    turtle.fd(width)
                color(x, y)
                cnt += 1
            turtle.penup()

        for i in list_squares:
            cnt = 0
            x = i.x
            y = i.y
            size = i.size

            turtle.setpos(x, y)
            turtle.pendown()
            while cnt < 5:
                turtle.fd(size)
                color(x, y)
                cnt += 1
            turtle.penup()

        turtle.exitonclick()
