"""

Class rectangle implements abstract class Shape

"""

__author__ = 'kozinvl'

from shape import Shape


class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__square = 0

    @property
    def square(self) -> float:
        """

        calculate rectangles' square

        """
        self.__square = self.__side_a * self.__side_b
        return self.__square


try:
    get_side_a = float(input('enter side a : '))
    get_side_b = float(input('enter side b : '))
    rectangle = Rectangle(get_side_a, get_side_b)
    print(rectangle.square)
except ValueError:
    print("Value error, not valid data entered")
except TypeError:
    print("TypeError: bad operand type")
