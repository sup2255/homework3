

import pytest
from decimal import Decimal
from calculator.calculation import Calculation

@pytest.fixture
def calc_fixture():
    return Calculation(Decimal('10'), Decimal('5'), 'add')

def test_calculation_init(calc_fixture):
    assert calc_fixture.a == Decimal('10')
    assert calc_fixture.b == Decimal('5')
    assert calc_fixture.operation == 'add'

def test_calculation_perform(calc_fixture):
    assert calc_fixture.perform() == Decimal('15')

def test_calculation_divide_by_zero():
    calc = Calculation(Decimal('10'), Decimal('0'), 'divide')
    with pytest.raises(ValueError):
        calc.perform()
