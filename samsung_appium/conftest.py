import pytest
from appium import webdriver


@pytest.fixture
def driver():

    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
        "automationName": "UiAutomator2",
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    login_button = driver.find_element("id", "login_button")
    login_button.click()
    driver.quit()
