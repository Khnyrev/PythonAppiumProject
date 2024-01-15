from appium.webdriver.common.appiumby import AppiumBy
from PythonAppiumProject.SessionStorage import session_storage
from PythonAppiumProject.Utils.element_helpers import wait_for_element
import time


class OnboardingPage:
    LOCATOR_SKIP_BUTTON = (AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button")

    def skip_onboarding_page(self):
        wait_result = wait_for_element(session_storage.get_session(),
                                       self.LOCATOR_SKIP_BUTTON,
                                       10,
                                       'LOCATOR_SKIP_BUTTON locator not found')
        wait_result.click()

