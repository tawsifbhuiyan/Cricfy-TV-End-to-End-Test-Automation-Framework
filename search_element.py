elements = driver.find_elements(AppiumBy.XPATH, "//*[contains(@text,'Live')]")

if len(elements) > 0:
    print("Element found")
else:
    print("Element not found")