import pytest


def test_addition():
    assert 2 + 2 == 4


def test_string():
    assert "hello".upper() == "HELLO"


def test_list():
    fruits = ["banana", "mango", "apple"]
    assert "banana" in fruits


def test_boolean():
    assert True is True


def test_multiple():
    assert 10 > 5
    assert 5 < 10


def test_dict():
    dict1 = {"name": "gagan", "age": 20}
    assert dict1["name"] == "gagan"
    assert dict1["age"] == 20


@pytest.mark.parametrize("x,y,result", [(2, 3, 5), (4, 5, 9), (10, 20, 30)])
def test_add(x, y, result):
    assert x + y == result
