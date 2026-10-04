import pytest
import sys


@pytest.mark.xfail
def test_a1():
    assert 5 + 5 == 10
    assert 5 - 5 == 0


@pytest.mark.skip(Reason="Sanity test")
def test_a2():
    assert 9 / 5 == 1.5, "failed test intentionally"


@pytest.mark.skip("reason=Smoke test")
def test_a3():
    assert 9 // 5 == 1  # interger truncating division


@pytest.mark.xfail(sys.platform == "linux", reason="works only in unix")
def test_gagan():
    assert 2 == 1
