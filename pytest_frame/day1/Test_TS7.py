import pytest


@pytest.mark.skipif(2 < 5, reason="skipping bcoz condition becomes true")
def test_firstProgram():
    print("this is first programe")


@pytest.mark.sanity
@pytest.mark.xfail
def test_secondProgram():
    print("This is second programe")
    assert 3 < 1


@pytest.mark.skip
def test_third():
    print("this is third programe")
