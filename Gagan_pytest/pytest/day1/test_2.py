import pytest


@pytest.mark.usefixtures("setup", "setup2", "setup3", "data_load")
class Test_Suite:
    def test_first(self):
        print("First program")

    def test_second(self):
        print("Second program")

    def test_third(self):
        print("Third program")


@pytest.mark.parametrize("x,y,result", [(1, 2, 3), (4, 5, 9)])
def test_sum(x, y, result):
    assert x + y == result


@pytest.mark.parametrize("x,y,result", [(5, 2, 3), (6, 4, 2), (7, 5, 2)])
def test_sub(x, y, result):
    assert x - y == result


@pytest.mark.parametrize("x,y,result", [(1, 2, 2), (2, 3, 6), (3, 4, 12)])
def test_mul(x, y, result):
    assert x * y == result


@pytest.mark.parametrize("x,y", [("hello", "HELLO")])
def test_upper(x, y):
    assert x.upper() == y
