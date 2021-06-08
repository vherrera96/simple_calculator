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
