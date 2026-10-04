import pytest
from utils.math_utils import add, subtract, multiply


@pytest.mark.smoke
def test_add():
    assert add(2, 3) == 5


@pytest.mark.regression
def test_multiply():
    assert multiply(3, 4) == 12
