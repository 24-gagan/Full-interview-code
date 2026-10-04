
import pytest

@pytest.mark.usefixtures("setup")
def test_func1():
    print("this is func1")

@pytest.mark.sanity
def test_func2():
    print("this is func2")

@pytest.mark.sanity
def test_func3():
    print("this is func3")