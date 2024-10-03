
from faker import Faker

fake = Faker()

def test_addition():
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    result = add(a, b)
    assert result == a + b


