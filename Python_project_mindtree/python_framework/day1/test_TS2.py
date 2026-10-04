import pytest


def test_func1():
    print("this is func1")


@pytest.mark.sanity
def test_func2():
    print("this is func2")


def test_func3():
    print("this is func3")
