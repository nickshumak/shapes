"""

Class rhombus implements abstract class Shape

"""

from shape import Shape


class Rhombus(Shape):
    """

    calculate the square of Rhombus

    """

    def __init__(self, diagonal_first, diagonal_second):
        self.__diagonal_first = diagonal_first
        self.__diagonal_second = diagonal_second
        self.__square = float()

    def square(self):
        self.__square = round(((self.__diagonal_first *
                                self.__diagonal_second)/2), 2)
        return self.__square

    def __repr__(self):
        return 'Square of user rhombus is {}'.format(self.__square)


try:
    diagonal_first = float(input("Enter a value for "
                                 "first diagonal of rhombus: "))
    diagonal_second = float(input("Enter a value for "
                                  "second diagonal of rhombus: "))

    if diagonal_first <= 0 or diagonal_second <= 0:
        print('Values for calculation are not positive. '
              'Restart and try again.')
        quit()

    user_rhombus = Rhombus(diagonal_first, diagonal_second)
    user_rhombus_square = user_rhombus.square()
    print(user_rhombus)
except ValueError:
    print("Value error, not valid data entered")
