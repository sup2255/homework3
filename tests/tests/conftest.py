import pytest
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int)

@pytest.fixture
def generate_test_data(request):
    num_records = request.config.getoption("--num_records")
    data = []
    for _ in range(num_records):
        a = fake.random_int(min=1, max=100)
        b = fake.random_int(min=1, max=100)
        operation = fake.random_element(elements=('add', 'subtract', 'multiply', 'divide'))
        data.append((a, b, operation))
    return data

