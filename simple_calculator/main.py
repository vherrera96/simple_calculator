from functools import reduce


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

    def mul(self, *args) -> int or float:
        """[summary]

        Returns:
            int or float: [description]
        """
        return reduce(lambda x, y: x * y, args)
