import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(2, 3) == 6

    def test_division_calculate_correctly(self):
        assert self.calc.division(6, 3) == 2

    def test_substraction_calculate_correctly(self):
        assert self.calc.subtraction(5, 3) == 2

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(6, 1) == 7
