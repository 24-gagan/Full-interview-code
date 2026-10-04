import pytest
from appium import webdriver


@pytest.fixture
def driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()


def test_login(driver):
    driver.find_element("id", "login_button").click()
    assert True


def test_send_text(driver):
    driver.find_element("id", "username").send_keys("test")
    assert True
