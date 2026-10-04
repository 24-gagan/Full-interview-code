import pytest
from app.utils import even, fact


@pytest.mark.parametrize(
    "n,expected", [(2, True), (3, False), (0, True), (-2, True), (-3, False)]
)
def test_is_even_parametrize(n, expected):
    assert even(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
    ],
)
def test_factorial_parametrized(n, expected):
    assert factorial(n) == expected
