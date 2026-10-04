import pytest


def test_func1():
    print("This is function")


@pytest.mark.sanity
def test_func2():
    print("This is function")


@pytest.mark.sanity
def test_func3():
    print("This is function")
