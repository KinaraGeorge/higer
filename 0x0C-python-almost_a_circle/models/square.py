#!/usr/bin/python3


from models.rectangle import Rectangle


class Square(Rectangle):


    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):

        return "[Square] (%d) %d/%d - %d" % (self.id,
                                             self.x,
                                             self.y,
                                             self.height)

    def update(self, *args, **kwargs):

        if len(args):
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                if index == 1:
                    self.size = value
                if index == 2:
                    self.x = value
                if index == 3:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):

        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}

    @property
    def size(self):

        return self.width

    @size.setter
    def size(self, value):

        self.width = value
        self.height = value
