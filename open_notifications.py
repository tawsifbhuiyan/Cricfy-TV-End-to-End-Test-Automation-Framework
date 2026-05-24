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

time.sleep(3)

# Test Case: Open notification panel
driver.open_notifications()

print("Notification panel test passed")

time.sleep(3)

driver.quit()