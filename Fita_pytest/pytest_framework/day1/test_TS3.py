import pytest


@pytest.mark.usefixtures("setup", "setup2")
class Test_Suite:

    def test_func1(self):
        print("This is func1")

    def test_func2(self):
        print("This is func2")

    def test_func3(self):
        print("This is func3")
