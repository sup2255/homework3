

from typing import List
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def get_latest(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def clear_history(cls):
        cls.history.clear()
