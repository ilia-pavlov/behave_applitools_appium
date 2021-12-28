import time


class Page:

    def __init__(self, driver, eyes):
        self.driver = driver
        self.eyes = eyes

    def find_element(self, *locator):
        time.sleep(1)
        return self.driver.find_element(*locator)
    
    def find_element_test_id(self, locator):
        time.sleep(1)
        return self.driver.find_element_by_accessibility_id(locator)

    def click(self, *locator):
        time.sleep(1)
        self.find_element(*locator).click()

    def click_by_test_id(self, locator):
        time.sleep(1)
        self.find_element_test_id(locator).click()

    def input(self, text, *locator):
        time.sleep(1)
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)
        
    def input_by_test_id(self, text, locator):
        time.sleep(1)
        element = self.find_element_test_id(locator)
        element.clear()
        element.send_keys(text)

