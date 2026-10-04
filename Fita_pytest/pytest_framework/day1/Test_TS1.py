import pytest


@pytest.mark.skipif(2 < 5, reason="skipping because condition becomes true")
def test_firstProgram():
    print("This is first program")


@pytest.mark.sanity
@pytest.mark.xfail
def test_secondProgram():
    print("This is second program")
    assert 3 < 1


@pytest.mark.skip
def test_third():
    print("This is second program")


def test_func1():
    print("This is func1")


@pytest.mark.sanity
def test_func2():
    print("This is func2")


def test_func3():
    print("This is func3")
