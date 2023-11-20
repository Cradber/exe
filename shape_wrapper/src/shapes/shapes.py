# shapes.py

from shapes import Triangle as _Triangle
from shapes import Rectangle as _Rectangle
from shapes import Circle as _Circle


class Triangle(_Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)


class Rectangle(_Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)


class Circle(_Circle):
    def __init__(self, radius):
        super().__init__(radius)
