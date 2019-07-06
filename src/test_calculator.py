"""
Unit Tests for the Calculator
"""

import calculator


class TestCalculator:
    def test_i_can_add_numbers(self):
        assert 4 == calculator.add(2, 2)

    def test_i_can_subtract_numbers(self):
        assert 3 == calculator.subtract(5, 2)

    def test_i_can_multipy_numbers(self):
        assert 20 == calculator.multiply(4, 5)
