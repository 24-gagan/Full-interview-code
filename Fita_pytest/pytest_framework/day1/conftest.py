import pytest


@pytest.fixture()
def setup():
    print("Login to app")
    yield
    print("Logout of app")


@pytest.fixture(scope="class")
def setup2():
    print("Launch browser")
    yield
    print("Exit Browser")
