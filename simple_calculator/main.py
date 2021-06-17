from functools import reduce
from typing import Union


class SimpleCalculator:
    def add(self, *args) -> int or float:
        """Performs the sum from the input.

        Returns:
            int or float: sum from input.
        """
        return sum(args)

    def sub(self, a: int or float, b: int or float) -> int or float:
        """Performs subtraction between two numbers

        Args:
            a (int or float): Subtract from.
            b (int or float): To subtract.

        Returns:
            int or float: Subtraction
        """
        return a - b

    def mul(self, *args) -> Union[int, float]:
        """Performs multiplication between numbers.

        Returns:
            Union[int, float]: Result of multiplication. Raise ValueError if any zero on args.
        """
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x * y, args)

    def div(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Performs division between a numbers.

        Args:
            a (Union[int, float]): Divides from.
            b (Union[int, float]): Divided by.

        Returns:
            Union[int, float]: Result of division of a by b. If b is zero result is inf.fe
        """
        try:
            return a/b
        except ZeroDivisionError:
            return float('inf')
