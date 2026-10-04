import pytest

@pytest.mark.xfail
def test_1():
    x=5
    y=5
    assert x==y

@pytest.mark.skip
def test_2():
    x=15
    y=33
    assert x+18==y
