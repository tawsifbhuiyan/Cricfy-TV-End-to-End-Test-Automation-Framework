from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# Setup
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "d3938a0b"
options.app_package = "app.cricfy.tv"
options.app_activity = ".MainActivity"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(3)

# Test Case: Swipe up multiple times
for i in range(3):
    driver.swipe(500, 1500, 500, 500, 800)
    print(f"Swipe Up Test {i+1} Passed")
    time.sleep(2)

print("Swipe up test completed successfully")

driver.quit()