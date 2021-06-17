import pytest
from simple_calculator.main import SimpleCalculator


def test_add_two_numbers():
    """Tests if add method behaves as expected"""
    calculator = SimpleCalculator()
    result = calculator.add(4, 5)
    assert result == 9, "Add 5 and 4 should be 9!"


def test_add_three_numbers():
    """Tests if the sum of three numbers behave as expected"""
    calculator = SimpleCalculator()
    result = calculator.add(4, 5, 6)
    assert result == 15, "Sum of 4,5 and 6 should be 15"


def test_add_many_numbers():
    """Tests if the sum of hundred numbers behave as expected"""
    numbers = range(100)
    calculator = SimpleCalculator()
    result = calculator.add(*numbers)
    assert result == 4950, "Sum of numbers from 1 to 100 should be 4950"


def test_subtract_two_numbers():
    """Tests if subtraction of two numbers behaves as expected"""
    calculator = SimpleCalculator()
    result = calculator.sub(10, 3)
    assert result == 7, "Subtract 3 from 10 should be 7"


def test_mul_two_numbers():
    """Test if multiplication of two numbers behaves as expected"""
    calculator = SimpleCalculator()
    result = calculator.mul(6, 4)
    assert result == 24


def test_mul_many_numbers():
    """Test if the multiplication of ten numbers behaves as expected"""
    numbers = range(1, 10)
    calculator = SimpleCalculator()
    result = calculator.mul(*numbers)
    assert result == 362880, "Multiplication of numbers from 1 to 9 should be 362880"
