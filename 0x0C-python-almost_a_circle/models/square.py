#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    def __str__(self):

        return("[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.width))

    @property
    def size(self):

        return self.width

    @size.setter
    def size(self, value):

        self.typeChecker("width", value)
        self.valueWHChecker("width", value)
        self.width = value

        self.typeChecker("height", value)
        self.valueWHChecker("height", value)
        self.height = value

    def update(self, *args, **kwargs):

        if len(args):
            for index, value in enumerate(args):
                if index is 0:
                    self.id = value
                elif index is 1:
                    self.size = value
                elif index is 2:
                    self.x = value
                elif index is 3:
                    self.y = value
                elif index >= 4:
                    raise Exception("WTF TOO MANY")
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs["id"]
                elif key == "size":
                    self.size = kwargs["size"]
                elif key == "x":
                    self.x = kwargs["x"]
                elif key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):

        temp = {}
        temp['id'] = self.id
        temp['size'] = self.size
        temp['x'] = self.x
        temp['y'] = self.y
        return temp
