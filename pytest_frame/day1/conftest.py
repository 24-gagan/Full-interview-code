# print("This is conftest")
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
    print("Exit browser")


@pytest.fixture(scope="module")
def setup3():
    print("Module level setup")
    yield
    print("Module level tear down")


@pytest.fixture(scope="module")
def setup4():
    print("Package level setup")
    yield
    print("Package level tear down")


@pytest.fixture()
def data_load():
    print("user data")
    return ["python", "java", "c++"]


pytest.fixture()


@pytest.fixture(params=["chrome", "ff", "ie"])
def run_browsers():
    print("user data")
