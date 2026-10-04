import pytest
import logging


@pytest.mark.parametrize("var1", [1, 2, 3])
def test_func1(var1):
    print("This is fuction 1")
    print(var1)


@pytest.mark.parametrize("var1,var2", [(1, 10), (2, 20), (3, 30)])
def test_func1(var1, var2):
    print("This is fuction 1")
    print(var1, var2)


print(logging.getLogger())
logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.error("this is error message")
