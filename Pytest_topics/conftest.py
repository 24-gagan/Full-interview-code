import pytest


def pytest_addoption(parser):
    parser.addoption("--cmdopt", default="QA")


@pytest.fixture()
def CmdOpt(pytestconfig):
    opt = pytestconfig.getoption("--cmdopt")
    if opt == "Prod":
        f = open(prod_config, "r")
    else:
        f = open(QA_config, "r")
