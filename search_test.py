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

# ------------------------
# 3️⃣ Wait until Search button is visible
# ------------------------
wait = WebDriverWait(driver, 20)  # wait up to 20 seconds
search_button = wait.until(
    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Search Channels"))
)
search_button.click()
time.sleep(1)

# ------------------------
# 4️⃣ Wait until search input appears
# ------------------------
search_input = wait.until(
    EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
)
search_input.send_keys("Mallorca")

# ------------------------
# 5️⃣ Press ENTER to search
# ------------------------
driver.press_keycode(66)  # KeyEvent 66 = Enter
time.sleep(2)

# ------------------------
# 6️⃣ Optional: verify a result
# ------------------------
try:
    result = driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'Mallorca')]")
    if result.is_displayed():
        print("✅ Search test PASSED")
    else:
        print("❌ Search test FAILED")
except:
    print("❌ Search test FAILED - no results found")

# ------------------------
# 7️⃣ Close the session
# ------------------------
driver.quit()