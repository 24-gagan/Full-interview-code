from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "11"
    options.device_name = "9620490701000TX"
    options.app = r"C:\Users\gagan\Downloads\android.wdio.native.app.v1.0.8.apk"
    options.automation_name = "UiAutomator2"
    options.no_reset = True

    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()
