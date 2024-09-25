

import pytest
from calculator.calculator import Calculator

def test_addition():
    assert Calculator.add(2, 2) == 4

def test_subtraction():
    assert Calculator.subtract(4, 2) == 2

def test_multiplication():
    assert Calculator.multiply(2, 3) == 6

def test_division():
    assert Calculator.divide(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(5, 0)
