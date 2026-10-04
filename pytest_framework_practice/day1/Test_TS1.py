import pytest


def test_function_program():
    print("First Program")


@pytest.mark.sanity
def test_function_second_program():
    print("Second Program")
