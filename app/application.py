from pages.launch_screen import LaunchScreen
from pages.login_screen import LoginScreen
from pages.home_dashboard import HomeDashboard


class Application:
    def __init__(self, driver, eyes):
        self.launch_screen = LaunchScreen(driver, eyes)
        self.login_screen = LoginScreen(driver, eyes)
        self.home_dashboard = HomeDashboard(driver, eyes)
