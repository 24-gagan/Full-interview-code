import pytest
from app.utils import even


@pytest.mark.smoke
def test_smoke_even():
    assert even(2) is True


@pytest.mark.regression
def test_regression_odd():
    assert even(3) is False
