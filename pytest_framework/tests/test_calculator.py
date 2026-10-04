import pytest
from utils.calculator import Calculator

@pytest.mark.smoke
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (10, -5, 5)
    ]
)
def test_addition(a, b, expected):
    calc = Calculator()
    assert calc.add(a, b) == expected


@pytest.mark.regression
def test_subtraction(setup):
    calc = Calculator()
    assert calc.sub(10, 5) == 5

def add(a,b):
    return a+b

def test_add(add):
    assert add(5,3)==8

@pytest.fixture(scope="module")
def connect():
    print("Database connected")
def close():
    print("Database closed")