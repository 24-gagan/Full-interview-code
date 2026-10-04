import pytest


@pytest.mark.smoke
def test_valid_login(db_fixture):
    assert db_fixture["user"] == "admin"
    assert db_fixture["password"] == "1234"


@pytest.mark.regression
def test_invalid_login(db_fixture):
    assert db_fixture["user"] != "guest"
