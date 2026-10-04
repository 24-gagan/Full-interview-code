import pytest


def test_func1():
    print("this is func1")


@pytest.mark.sanity
@pytest.mark.parametrize("var1,var2", [(1, 10), (2, 20), (3, 30)])
def test_func2(var1, var2):
    print("this is func2")
    print(var1, var2)


@pytest.mark.sanity
def test_func3():
    print("this is func3")
