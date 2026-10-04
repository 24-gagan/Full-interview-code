import pytest


@pytest.fixture
def sample_user():
    return {"username": "admin", "password": "secret"}
