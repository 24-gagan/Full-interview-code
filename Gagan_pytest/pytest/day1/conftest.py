import pytest


@pytest.fixture()
def setup():
    print("Login to app")
    yield
    print("Logout from app")


@pytest.fixture(scope="class")
def setup2():
    print("Launch browser")
    yield
    print("Exit browser")


@pytest.fixture(scope="module")
def setup3():
    print("Module level setup")
    yield
    print("Module level teardown")


@pytest.fixture()
def data_load():
    print("User data")
    return ["python", "java", "C++"]


@pytest.fixture(scope="class")
def data_load2():
    print("Launch browser")
    yield
    print("Exit browser")
