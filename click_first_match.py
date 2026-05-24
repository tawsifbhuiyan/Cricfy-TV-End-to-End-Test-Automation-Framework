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
    time.sleep(2)
    print("✅ Navigated to Live section")
except:
    print("❌ Could not find Live section")
    driver.quit()
    exit()

# ------------------------
# 4️⃣ Click the first live match
# ------------------------
try:
    # Using class and index
    first_match = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").index(1)')
        )
    )
    first_match.click()
    print("➡ Clicked the first live match")
    time.sleep(3)
except:
    print("❌ Could not click the first live match - check index/class in Inspector")

# ------------------------
# 5️⃣ Close session
# ------------------------
driver.quit()










