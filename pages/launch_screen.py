from pages.base_page import Page
from selenium.webdriver.common.by import By
from features.strings.eyes import *
from features.strings.locaters import *



class LaunchScreen(Page):

    GET_STARTED_TEST_ID = GET_STARTED
    INFO_ICON_XPATH = (By.XPATH, INFO_ICON )
    CANCEL_CTA_XPATH = (By.XPATH, CANCEL_CTA)
    WELCOME_SCREEN_XPATH = (By.XPATH, WELCOME_SCREEN)

    def tap_get_started(self):
        self.click_by_test_id(self.GET_STARTED_TEST_ID)
       # self.eyes.check_window(ACCESS_CODE_PAGE)


    def tap_info_icon(self):
        self.click(*self.INFO_ICON_XPATH)
       # self.eyes.check_window(INFO_PAGE)


    def tap_cancel_cta(self):
        self.click(*self.CANCEL_CTA_XPATH)


    def assert_welcome_screen(self, title):
        actual_text = self.find_element(*self.WELCOME_SCREEN_XPATH).text
        expected_text = title

        assert expected_text == actual_text, f"Error. Expected text '{expected_text}, but actual text: '{actual_text}"
