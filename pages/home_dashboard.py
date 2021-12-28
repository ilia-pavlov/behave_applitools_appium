from pages.base_page import Page
from selenium.webdriver.common.by import By


class HomeDashboard(Page):
    HEALTH_ASSESSMENT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout" \
                         "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android" \
                         ".view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android" \
                         ".view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android" \
                         ".view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup" \
                         "/android.view.ViewGroup[2]/android.widget.TextView ")

    def verify_login_state(self, title: str):
        expected_text = self.find_element(*self.HEALTH_ASSESSMENT).text
        assert title in expected_text, f'Expected {expected_text} to be in {title} '
