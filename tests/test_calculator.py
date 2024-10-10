import pytest
from faker import Faker
from calculator import Calculator

fake = Faker()

def test_add():
    calc = Calculator()
    a = fake.random_number(digits=3)
    b = fake.random_number(digits=3)
    assert calc.add(a, b) == a + b

def test_subtract():
    calc = Calculator()
    a = fake.random_number(digits=3)
    b = fake.random_number(digits=3)
    assert calc.subtract(a, b) == a - b

def test_multiply():
    calc = Calculator()
    a = fake.random_number(digits=2)
    b = fake.random_number(digits=2)
    assert calc.multiply(a, b) == a * b

def test_divide():
    calc = Calculator()
    a = fake.random_number(digits=3)
    b = fake.random_number(digits=2, nonzero=True)
    assert calc.divide(a, b) == pytest.approx(a / b)

def test_divide_by_zero():
    calc = Calculator()
    a = fake.random_number(digits=3)
    with pytest.raises(ValueError):
        calc.divide(a, 0)
