import pytest


@pytest.fixture()
def setup_list():
    print("]n in fixtures..\n")
    city = ["New York", "London", "Rihana", "Singapore", "Mumbai"]
    return city


def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == "New York"
    assert setup_list[::2] == ["New York", "Rihana", "Mumbai"]


def test_reverseList(setup_list):
    assert setup_list[::-2] == ["Mumbai", "Rihana", "New York"]


@pytest.mark.usefixtures("setup_list")
def test_usefixturedemo():
    assert 1 == 2
