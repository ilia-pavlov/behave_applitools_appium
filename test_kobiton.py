from appium import webdriver
import time
from selenium.webdriver.remote.remote_connection import RemoteConnection


desired_caps = {
    'sessionName': 'Automation test session',
    'sessionDescription': '',
    'deviceOrientation': 'portrait',
    'captureScreenshots': True,
    'app': 'XXXXXXXXXXXXXXXXXX',
    'deviceGroup': 'KOBITON',
    'deviceName': 'Galaxy S9',
    'platformName': 'Android',
    'platformVersion': '8.0.0'
}

APPIUM_HUB = 'http://127.0.0.1:4723/wd/hub'
GET_STARTED_BUTTON = "marketing-animation-sign-up-button"
ACCESS_CODE_FILED = "sign-up-code-input"
ACCESS_CODE = 'XXXXXXXXXXX'


kobitonServerUrl = 'https://XXXXXXXXXXXXXX@api.kobiton.com/wd/hub'

# session_timeout = 120
# _command_executor = RemoteConnection(kobitonServerUrl)
# _command_executor.set_timeout(session_timeout)

#driver = webdriver.Remote(_command_executor, desired_caps)

    

driver = webdriver.Remote(kobitonServerUrl, desired_capabilities=desired_caps)
driver.implicitly_wait(120)

def tap(element):
    driver.find_element_by_accessibility_id(element).click()
def input(element, text):
    input_filed = driver.find_element_by_accessibility_id(element)
    time.sleep(1)
    input_filed.clear()
    input_filed.send_keys(text)


tap(GET_STARTED_BUTTON)
input(ACCESS_CODE_FILED, ACCESS_CODE)
driver.quit()
