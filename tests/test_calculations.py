

from decimal import Decimal
from calculator.calculation import Calculation
from calculator.calculations import Calculations

def test_add_calculation():
    calc = Calculation(Decimal('10'), Decimal('5'), 'add')
    Calculations.add_calculation(calc)
    assert len(Calculations.history) == 1

def test_get_latest():
    calc1 = Calculation(Decimal('10'), Decimal('5'), 'add')
    calc2 = Calculation(Decimal('20'), Decimal('3'), 'multiply')
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    assert Calculations.get_latest() == calc2

def test_clear_history():
    calc = Calculation(Decimal('10'), Decimal('5'), 'add')
    Calculations.add_calculation(calc)
    Calculations.clear_history()
    assert len(Calculations.history) == 0
