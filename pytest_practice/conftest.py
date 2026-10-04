import pytest


@pytest.fixture(scope="function")
def db_fixture():
    print("\n[Setup] Connect to DB")
    data = {"user": "admin", "password": "1234"}
    yield data
    print("\n[Teardown] Disconnect DB")
