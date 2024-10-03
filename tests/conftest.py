def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int,
                     help="Number of records to generate for testing")

def pytest_generate_tests(metafunc):
    if "num_records" in metafunc.fixturenames:
        num_records = metafunc.config.getoption("num_records")
        metafunc.parametrize("num_records", [num_records])
