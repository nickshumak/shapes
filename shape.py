"""

This is an abstract class from which all shapes will be inherited

"""

__author__ = 'nshumakov'

from abc import ABCMeta, abstractmethod, abstractproperty


class Shape():
    __metaclass__ = ABCMeta

    @abstractmethod
    def square(self) -> float:
        """

        implementation of the method of calculating the area of its shape
        :return: square

        """