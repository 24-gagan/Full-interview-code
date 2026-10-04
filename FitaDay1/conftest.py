# print("this is conftest")
import pytest

@pytest.fixture()# default scope = func/module
def setup():
    print("Login to app")
    yield
    print("Logout of app")

@pytest.fixture(scope="class")
def setup2():
    print("launch browser")
    yield
    print("exit browser")

@pytest.fixture(scope="module")#
def setup3():
    print("Module level setup")
    yield
    print("Module level tear down")


@pytest.fixture(scope="package")#
def setup4():
    print("package level setup")
    yield
    print("package level tear down")


##data driven using fixture

@pytest.fixture()
def data_load():
    print("user data")
    return ["python", "java", "c++"]

# @pytest.fixture(params=[("chrome", "name1"), ("ff","name2"), ("ie", "name3")])
@pytest.fixture(params=["chrome", "ff", "ie"])
def run_browsers(request):
    print("user data")
    return request.param