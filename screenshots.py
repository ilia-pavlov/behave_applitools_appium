import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desire_capabilities = {
    "deviceName": "CT-Phone-023",
    "platformVersion": "14.4",
    "platformName": "iOS",
    "udid": "XXXXXXXXXXXXXXXX",
    "app": "XXXXXXXXXXXXX",
    "automationName": "XCUITest",
    "noReset": "true"  # true
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desire_capabilities)
driver.implicitly_wait(10)

SCREENSHOTS_REP = 'PATH/XXXXXXX'
FORMAT = '.png'
ts = time.strftime(' %Y_%m_%d_%H%M%S')

home_screen = 'home_screen ' + ts
home_screen_sh = driver.save_screenshot(SCREENSHOTS_REP + home_screen + FORMAT)


progress_button = driver.find_element(by=MobileBy.IOS_CLASS_CHAIN,
                                      value='**/XCUIElementTypeOther[`label == "Progress"`][2]')
progress_button.click()

progress_screen_tittle = WebDriverWait(driver, 20) \
    .until(EC.presence_of_element_located((MobileBy.IOS_PREDICATE,
                                           'label == "Progress" AND name == "Progress" '
                                           'AND value == "Progress"')))

progress_screen = 'progress_screen ' + ts
progress_screen_sh = driver.save_screenshot(SCREENSHOTS_REP + progress_screen + FORMAT)

driver.quit()
