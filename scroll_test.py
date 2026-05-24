from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
import time

# ------------------------
# 1️⃣ Setup Appium options
# ------------------------
options = UiAutomator2Options()
options.automation_name = "UiAutomator2"
options.platform_name = "Android"
options.platform_version = "11"
options.device_name = "d3938a0b"
options.app_package = "app.cricfy.tv"
options.app_activity = ".MainActivity"
options.no_reset = True
options.ignore_hidden_api_policy_error = True

# ------------------------
# 2️⃣ Connect to Appium Server
# ------------------------
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 20)

# ------------------------
# 3️⃣ Navigate to Live section
# ------------------------
try:
    live_tab = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text,'Live')]"))
    )
    live_tab.click()
    time.sleep(1)
    print("✅ Navigated to Live section")
except:
    print("❌ Could not find Live section")
    driver.quit()
    exit()

# ------------------------
# 4️⃣ Scroll and click each match
# ------------------------
# Function to click all matches currently visible
def click_visible_matches():
    matches = driver.find_elements(AppiumBy.XPATH, "//*[@resource-id='app.cricfy.tv:id/match_card']")
    for match in matches:
        try:
            print("➡ Clicking match:", match.text)
            match.click()
            time.sleep(2)  # wait inside match
            driver.back()   # go back to Live section
            time.sleep(1)
        except:
            print("❌ Could not click this match")

# Scroll loop
for i in range(5):  # number of scrolls, adjust as needed
    click_visible_matches()
    # Swipe up to load more matches
    driver.swipe(500, 1500, 500, 500, 800)
    time.sleep(1)

print("✅ Finished clicking all visible matches")
driver.quit()