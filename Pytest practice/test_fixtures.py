import pytest


@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 25
    return [a, b, c]


@pytest.mark.smoke
def test_method1(numbers):
    x = 15
    assert numbers[0] == x


@pytest.fixture
def db_fixture(numbers):
    print("setup open the database")
    yield
    print("teardown close the database")


@pytest.mark.regression
def test_database(db_fixture):
    print("test case running")
