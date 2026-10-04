import pytest


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def test_add():
    assert add(1, 3) == 4


def test_mul():
    assert mul(2, 3) == 6
