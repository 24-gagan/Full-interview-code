from app.utils import login


def test_login_with_fixture(sample_user):
    assert login(sample_user["username"], sample_user["password"]) is True
