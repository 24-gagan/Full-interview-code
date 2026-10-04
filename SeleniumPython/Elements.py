import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://trytestingthis.netlify.app/")
time.sleep(2)

driver.find_element(By.ID, "fname").send_keys("Gagan")
driver.find_element(By.ID, "lname").send_keys("deep Singh")

# Correct locator for submit button
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class-'btn btn-sucess']").click()


time.sleep(3)
driver.quit()
