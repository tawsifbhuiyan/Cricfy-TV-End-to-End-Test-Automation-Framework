from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "d3938a0b"
options.app_package = "app.cricfy.tv"
options.app_activity = ".MainActivity"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(5)

# First go down
driver.swipe(500, 1500, 500, 500, 800)
time.sleep(2)

# Test Case: Swipe down
driver.swipe(500, 500, 500, 1500, 800)

print("Swipe down test passed")

time.sleep(2)

driver.quit()