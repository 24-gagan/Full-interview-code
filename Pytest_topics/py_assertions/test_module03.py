import pytest


def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0


def func1():
    raise ValueError("Exceptopn func1 raised")


def test_case02():
    with pytest.raises(Exception) as excinfo:
        # assert (1, 2, 3) == (1, 2, 3)
        func1()
    print(str(excinfo))
