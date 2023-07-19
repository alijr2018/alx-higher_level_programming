#!/usr/bin/python3

"""Write the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of the Square"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Getter for size attribute"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign attributes based on *args and **kwargs"""
        if args:
            attr_names = ['id', 'size', 'x', 'y']
            for idx, arg in enumerate(args):
                setattr(self, attr_names[idx], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
