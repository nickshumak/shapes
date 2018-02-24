"""

Class circle implements abstract class Shape

"""

from shape import Shape
from math import pi

__author__ = 'nshumakov'


class Circle(Shape):
    """

    calculate the square of Circle

    """

    def __init__(self, radius):
        self.__radius = radius
        self.__square = 0

    def square(self) -> float:
        self.__square = pi * (self.__radius ** 2)
        return self.__square


try:
    first_circle = Circle(float(input("Enter radius of circle:" + "\n")))
    print(first_circle.square())
except ValueError:
    print("Value error, not valid data entered")
except TypeError:
    print("TypeError: bad operand type")

