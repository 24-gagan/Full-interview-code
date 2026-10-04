import pytest

# -------------------------
# BASIC FIXTURE
# -------------------------
@pytest.fixture
def setup():
    print("\nSetup executed")
    yield
    print("\nTeardown executed")


# -------------------------
# FIXTURE WITH SCOPE
# -------------------------
@pytest.fixture(scope="module")
def module_setup():
    print("\nModule setup")
    yield
    print("\nModule teardown")


@pytest.fixture(scope="session")
def session_setup():
    print("\nSession setup")
    yield
    print("\nSession teardown")


# -------------------------
# FIXTURE WITH PARAMETER
# -------------------------
@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    return request.param


# -------------------------
# HOOK: TEST START
# -------------------------
def pytest_runtest_setup(item):
    print(f"\nStarting test: {item.name}")


# -------------------------
# HOOK: TEST FINISH
# -------------------------
def pytest_runtest_teardown(item):
    print(f"\nFinished test: {item.name}")
