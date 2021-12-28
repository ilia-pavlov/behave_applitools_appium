from appium import webdriver
from app.application import Application
from applitools.selenium import Eyes
from features.strings.config import *
from features.strings.eyes import PROJECT, LAUNCH_PAGE, TEST_NAME


def before_scenario(context, scenario):

    context.driver = driver_setup(SAMSUNG_S9)
    context.eyes = initialise_eyes() # Initialize the eyes SDK and set your private API key.

    context.eyes.open(driver=context.driver, app_name=PROJECT, test_name=TEST_NAME)
    context.app = Application(context.driver, context.eyes)

    context.eyes.check_window(LAUNCH_PAGE)

def after_scenario(context, scenario):
    context.driver.quit()
    context.eyes.abort_if_not_closed()


def initialise_eyes():
    eyes = Eyes()
    eyes.api_key = EYES_IPA_KEY
    return eyes

def driver_setup(device):
    driver = webdriver.Remote(APPIUM_HUB, desired_capabilities=device)
    driver.implicitly_wait(20)
    return driver


