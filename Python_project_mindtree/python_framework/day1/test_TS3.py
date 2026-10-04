import pytest


@pytest.fixture()
def setup():
    print("Login to app")
    yield
    print("Logout to app")


def test_firstProgram(setup):
    print("This is first program")


def test_secondProgram(setup):
    print("This is second program")
    assert 3 < 1


def test_third(setup):
    print("This is third program")
