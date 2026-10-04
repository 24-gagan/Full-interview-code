import pytest


@pytest.mark.skipif("2 < 5", reason="skipping bcoz condition becomes True")
def test_firstProgram():
    print("This is first program")


@pytest.mark.sanity
@pytest.mark.xfail
def test_secondProgram():
    print("This is second program")
    assert 3 < 1


@pytest.mark.skip
def test_third():
    print("This is third program")
