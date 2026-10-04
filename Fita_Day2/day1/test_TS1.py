import pytest
import logging

@pytest.mark.skipif(2<5, reason="skipping bcoz condition becomes true")
def test_firstProgram():
    print("this is first programe")

@pytest.mark.sanity
@pytest.mark.xfail
def test_secondProgram():
    print("this is second programe")
    assert 3<1

@pytest.mark.skip
def test_third():
    print("this is second programe")

def test_func1():
    logging.warning("this is func1")

@pytest.mark.sanity
def test_func2():
    logging.warning("this is func2")

@pytest.mark.sanity
def test_func3():
    logging.warning("this is func3")