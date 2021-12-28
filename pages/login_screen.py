from pages.base_page import Page
from selenium.webdriver.common.by import By


class LoginScreen(Page):
    # use this way to explain why you want to add testID's to element, works flaky - only for DEMO
    LOGIN_BUTTON = (
        By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android" \
                  ".widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup" \
                  "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android" \
                  ".view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view" \
                  ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" \
                  "1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup" \
                  "/android.view.ViewGroup[3] ")
    EMAIL_FILED = (
        By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                  "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view"
                  ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view"
                  ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view"
                  ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup["
                  "1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup"
                  "/android.view.ViewGroup[1]/android.widget.EditText")

    PASSWORD_FILED = (
        By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout" \
                  "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view" \
                  ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view" \
                  ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view" \
                  ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" \
                  "1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup" \
                  "/android.view.ViewGroup[2]/android.widget.EditText ")

    def input_email(self, valid_email_dev: str):
        self.input(valid_email_dev, self.EMAIL_FILED)

    def input_password(self, valid_password: str):
        self.input(valid_password, self.PASSWORD_FILED)

    def tap_login_button(self):
        self.click(*self.LOGIN_BUTTON)
