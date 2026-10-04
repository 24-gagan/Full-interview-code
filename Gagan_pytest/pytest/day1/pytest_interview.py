import pytest


def test_addition():
    assert 2 + 3 == 5


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (1, 3, 4),
        (1, 4, 5),
    ],
)
def test_add(a, b, expected):
    assert a + b == expected


@pytest.fixture
def return_fixture():
    print("open browser")
    yield
    print("close browser")


def test_user(return_fixture):
    assert 2 + 3 == 5


@pytest.mark.skip(reason="Feature not available")
def test_skip(return_fixture):
    assert True


@pytest.mark.xfail(reason="Feature not available")
def test_xfail(return_fixture):
    assert 2 + 1 == 5


def test_status_sounrcecode():
    status_code = 200
    assert status_code == 200


def test_string():
    str1 = "gagan"
    assert str1.upper() == "GAGAN"


def test_list():
    list1 = ["apple", "mange", "orange"]
    assert "apple" in list1


import pytest


@pytest.fixture
def setup():
    print("Browser Open")
    yield
    print("Browser Close")


import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_login():
    assert True


def test_login(setup):
    print("Login Successful")
