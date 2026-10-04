import pytest
from app.utils import even, fact, login


def test_is_even():
    assert even(2) == True


def test_is_even_false():
    assert even(7) == False


def test_fact():
    assert fact(5) == 120


def test_login_success():
    assert login("admin", "secret") == True


def test_login_failure():
    assert login("admin", "wrong") == False
