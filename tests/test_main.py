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


def test_div_two_numbers_float():
    """Tests if the division of two numbers is a float"""
    calculator = SimpleCalculator()
    result = calculator.div(13, 2)
    assert result == 6.5, "13 divided by 2 is 6.5!"


def test_div_by_zero_returns_inf():
    """Tests if division by 0 return inf."""
    calculator = SimpleCalculator()
    result = calculator.div(5, 0)
    assert result == float('inf')


def test_mul_by_zero_raises_expection():
    """Tests if multiplication by raise a ValueError."""
    calculator = SimpleCalculator()
    with pytest.raises(ValueError):
        calculator.mul(3, 0)


def test_avg():
    """Tests average computation, with no threshold"""
    calculator = SimpleCalculator()
    assert calculator.avg([2, 5, 12, 98]) == 29.25


def test_avg_upper_threshold():
    """Tests average computation with upper threshold"""
    calculator = SimpleCalculator()
    assert calculator.avg([2, 5, 12, 98], ut=90) == calculator.avg([2, 5, 12])


def test_avg_lower_threshold():
    """Tests average computation with lower threshold"""
    calculator = SimpleCalculator()
    assert calculator.avg([2, 5, 12, 98], lt=10) == calculator.avg([12, 98])


def test_avg_upper_threshold_not_included():
    """Tests that the upper threshold is not included when removing outliers"""
    calculator = SimpleCalculator()
    assert calculator.avg([2, 5, 12, 98], ut=12) == calculator.avg([2, 5, 12])


def test_avg_lower_threshold_not_included():
    """Tests if the lower threshold is not included when removing data"""
    calculator = SimpleCalculator()
    assert calculator.avg([2, 5, 12, 98], lt=5) == calculator.avg([5, 12, 98])


def test_avg_empty_list():
    """Tests if avg works with an empty list"""
    calculator = SimpleCalculator()
    assert calculator.avg([]) == 0


def test_avg_empty_after_outlier_removal():
    """Test if avg works if the list is empty after outlier removal"""
    calculator = SimpleCalculator()
    assert calculator.avg([12, 98], lt=15, ut=90) == 0


def test_avg_empty_list_with_outlier_removal():
    """Test if avg works if the list is empty before outlier removal"""
    calculator = SimpleCalculator()
    assert calculator.avg([], lt=15, ut=90) == 0
