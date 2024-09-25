
from decimal import Decimal

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: str):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self) -> Decimal:
        if self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'subtract':
            return self.a - self.b
        elif self.operation == 'multiply':
            return self.a * self.b
        elif self.operation == 'divide':
            if self.b == 0:
                raise ValueError("Cannot divide by zero")
            return self.a / self.b
        else:
            raise ValueError(f"Unknown operation: {self.operation}")
