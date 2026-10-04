import pytest


# launch app test
def test_launch_app(driver):
    assert driver.is_app_installed("com.android.settings")


# check page title/Activity
def test_current_activity(driver):
    assert "settings" in driver.current_activity
