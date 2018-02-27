"""

Class triangle implements abstract class Shape

"""

__author__ = 'riabchenko'

from shape import Shape


class Triangle(Shape):
    def __init__(self, side_1, side_2, side_3):
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3
        self.__square = 0

    @property
    def square(self) -> float:
        """

        calculate triangle's square

        """
        semi_perimeter = (self.__side_1 + self.__side_2 + self.__side_3)/2
        self.__square = (semi_perimeter *(semi_perimeter - self.__side_1)*
                         (semi_perimeter - self.__side_2)*
                         (semi_perimeter - self.__side_3))**0.5
        return self.__square


try:
    get_side_1 = float(input('enter side 1 : '))
    get_side_2 = float(input('enter side 2 : '))
    get_side_3 = float(input('enter side 3 : '))
    triangle = Triangle(get_side_1, get_side_2, get_side_3)
    print(triangle.square)
except ValueError:
    print("Value error, not valid data entered")
except TypeError:
    print("TypeError: bad operand type")