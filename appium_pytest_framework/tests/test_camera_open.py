# tests/test_open_app.py
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy

def test_open_app(driver):
    time.sleep(5)
    try:
        main_element = driver.find_element(AppiumBy.ID, "android:id/content")
        assert main_element.is_displayed()
    except:
        pytest.fail("App did NOT open or element not found")

# Function to navigate to login page

def navigate_to_login_page(driver):
    """
    Navigate to the login page of the app.
    Update the locators based on your app's UI.
    """
    wait = WebDriverWait(driver, 10)
    try:
        # Example: Click on the Menu button if your app has one
        menu_button = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "menu_button"))
        )
        menu_button.click()

        # Click on the Login button
        login_button = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "login_button"))
        )
        login_button.click()

        # Verify Login page opened (example: check username field)
        username_field = wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "username_input"))
        )
        assert username_field.is_displayed()
        print("Navigated to login page successfully.")

    except Exception as e:
        pytest.fail(f"Failed to navigate to login page: {e}")

# Optional: Test combining both
def test_open_and_navigate_login(driver):
    test_open_app(driver)
    navigate_to_login_page(driver)