from appium.webdriver.common.appiumby import AppiumBy
from PythonAppiumProject.pages.base_page import BasePage


class OnboardingPage(BasePage):

    def skip_onboarding(self):
        skip_button_locator = (AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button")
        skip_button = self.wait_for_element(skip_button_locator, 10, 'не нашли skip_button_locator')
        return skip_button.click()
