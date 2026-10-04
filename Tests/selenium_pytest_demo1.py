import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_google_search():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://trytestingthis.netlify.app/")
    time.sleep(2)

    driver.find_element(By.ID, "fname").send_keys("Gagan")
    driver.find_element(By.ID, "lname").send_keys("deep Singh")

    time.sleep(2)

    # Correct locator for submit button
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    time.sleep(3)
    driver.quit()
