import pytest


@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    assert False


@pytest.mark.xfail(reason="Known bug: division rounding")
def test_known_bug():
    assert 1 / 3 == 0.33
