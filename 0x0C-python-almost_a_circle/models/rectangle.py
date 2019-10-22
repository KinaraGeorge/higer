#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def integer_validator(self, name, value):

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and (name is "height" or name is "width"):
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and (name is "x" or name is "y"):
            raise ValueError("{} must be >= 0".format(name))

    def area(self):

        return self.width * self.height

    def display(self):

        print(("\n" * self.y) + "\n".join((" " * self.x) +
                                          ("#" * self.width)
                                          for row in range(self.height)))

    def __str__(self):

        return "[%s] (%s) %d/%d - %d/%d" % (type(self).__name__,
                                            self.id,
                                            self.x,
                                            self.y,
                                            self.width,
                                            self.height)

    def update(self, *args, **kwargs):

        if len(args):
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                if index == 1:
                    self.width = value
                if index == 2:
                    self.height = value
                if index == 3:
                    self.x = value
                if index == 4:
                    self.y = value
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs["id"]
                if key == "width":
                    self.width = kwargs["width"]
                if key == "height":
                    self.height = kwargs["height"]
                if key == "x":
                    self.x = kwargs["x"]
                if key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):

        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}

    @property
    def width(self):

        return self.__width

    @property
    def height(self):

        return self.__height

    @property
    def x(self):

        return self.__x

    @property
    def y(self):

        return self.__y

    @width.setter
    def width(self, value):

        self.integer_validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):

        self.integer_validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):

        self.integer_validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):

        self.integer_validator("y", value)
        self.__y = value
