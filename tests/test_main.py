from simple_calculator.main import SimpleCalculator


def test_add_two_numbers():
    """Tests if add method behaves as expected"""
    calculator = SimpleCalculator()
    result = calculator.add(4, 5)
    assert result == 9, "Add 5 and 4 should be 9!"
