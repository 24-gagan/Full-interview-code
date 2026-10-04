import pytest


def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


def test_divisible_by_6(input_value):
    assert input_value % 6 == 0


def test_divisible_by_13(input_value):
    assert input_value % 13 == 0


@pytest.mark.parametrize("num,output", [(1, 11), (2, 22), (3, 35), (4, 44)])
def test_multiplication(num, output):
    assert 11 * num == output
