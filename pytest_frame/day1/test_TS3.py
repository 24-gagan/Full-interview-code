import pytest


@pytest.mark.usefixtures("setup", "setup2", "setup3", "setup4", "run_browsers")
class Test_Suite:

    def test_firstProgram(self, data_load):
        print(data_load)
        print("this is first programe")

    def test_secondProgram(self):
        print("This is second programe")

    def test_third(self):
        print("this is third programe")
