import pytest


@pytest.mark.parametrize("var1", [1, 2, 3])
def test_func1(var1):
    print("This is func1")
    print(var1)


@pytest.mark.sanity
@pytest.mark.parametrize("var1,var2", [(1, 10), (2, 20), (3, 30)])
def test_func2(var1, var2):
    print("This is func2")
    print(var1, var2)


def test_func3():
    print("This is func3")
