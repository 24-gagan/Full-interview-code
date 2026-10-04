from app.calculator_gui import add


def test_add_function():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, 3) == 1
