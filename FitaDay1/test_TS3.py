import pytest

from pytest_framework.day1.conftest import data_load


# @pytest.fixture()
# def setup():
#     print("Login to app")
#     yield
#     print("Logout of app")

@pytest.mark.usefixtures("setup", "setup2", "setup3", "setup4","data_load")
class Test_Suite:
    def test_firstProgram(self,data_load):
        print("this is first programe")
        print(data_load[0])

    def test_secondProgram(self, run_browsers):
        print("this is second programe")
        print(run_browsers)

    def test_third(self):
        print("this is third programe")