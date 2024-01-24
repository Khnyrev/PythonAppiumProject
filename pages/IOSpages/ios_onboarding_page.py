from appium.webdriver.common.appiumby import AppiumBy
from PythonAppiumProject.SessionStorage import session_storage
from PythonAppiumProject.Utils.element_helpers import wait_for_element
import time


class IOSOnboardingPage:
    LOCATOR_SKIP_BUTTON = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Skip"`]')

    def skip_onboarding_page(self):
        # print(f'########## GDE LOCATOR? COVALSKI {self.LOCATOR_SKIP_BUTTON}#########')
        wait_result = wait_for_element(session_storage.get_session(),
                                       self.LOCATOR_SKIP_BUTTON,
                                       10,
                                       'LOCATOR_SKIP_BUTTON locator not found')
        wait_result.click()
        # driver = session_storage.get_session()
        # device_info = driver.current_context
        #
        # print(f'########## device_info is {device_info} #######################')

