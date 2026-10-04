import pytest
import logging

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


def test_addition():
    logger.warning("Addition test executed")
    assert 2 + 3 == 5


@pytest.mark.skip
def test_subtraction():
    assert 10 - 4 == 6


@pytest.mark.xfail
def test_str():
    assert "gagan".upper() == "Gagan"


@pytest.mark.skipif(2 < 5, reason="skip if condition is true")
def test_mul():
    logger.warning("Multiplication test")
    assert 2 * 3 == 6


@pytest.mark.sanity
@pytest.mark.xfail
def test_sub():
    assert 10 - 4 == 7


@pytest.mark.sanity
@pytest.mark.parametrize("var1,var2", [(1, 10), (2, 20), (3, 30)])
def test_func2(var1, var2):
    logger.warning(f"Values are {var1} and {var2}")
    print(var1, var2)


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    return request.param


with pytest.raises(ZeroDivisionError):
    10 / 0
