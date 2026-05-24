from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "d3938a0b"
options.app_package = "app.cricfy.tv"
options.app_activity = ".MainActivity"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

wait = WebDriverWait(driver, 20)

# Open Live tab
live = wait.until(
    EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text,'Live')]"))
)

live.click()

time.sleep(2)

# Back navigation test
driver.back()

print("Back navigation test passed")

time.sleep(2)

driver.quit()