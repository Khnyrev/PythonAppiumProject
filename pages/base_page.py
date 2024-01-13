import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException


# def get_locator_string(locator_with_type):
#     exploded_locator = locator_with_type.split(":")
#     locator_type = exploded_locator[0]
#     locator_body = exploded_locator[1]
#
#     if locator_type == "xpath":
#         return AppiumBy.XPATH, locator_body
#     elif locator_type == "id":
#         return AppiumBy.ID, locator_body
#     elif locator_type == "accessibility id":
#         return AppiumBy.ACCESSIBILITY_ID, locator_body


class BasePage:
    LOCATOR_GO_BACK_BUTTON = 'Navigate up'
    LOCATOR_GO_BACK_BUTTON_TYPE = AppiumBy.ACCESSIBILITY_ID

    def __init__(self, get_driver):
        self.driver = get_driver

    def wait_for_element(self, locator, timeout=20, error_message="текст по умолчанию"):
        wait_result = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                                error_message)
        return wait_result

    def wait_for_element_and_click(self, locator, timeout=20,
                                   error_message="текст по умолчанию"):
        wait_result = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                                error_message)
        return wait_result.click()

    def count_searched_elements(self, locator, locator_type, timeout=20, error_message="текст по умолчанию"):
        count_result = self.driver.find_elements(locator_type, locator)
        print(len(count_result))
        return len(count_result)

    def back_to_previous_screen(self):
        go_back = self.driver.find_element(BasePage.LOCATOR_GO_BACK_BUTTON_TYPE, BasePage.LOCATOR_GO_BACK_BUTTON)
        return go_back.click()

    def wait_for_element_to_disappear(self, locator, timeout=20,
                                      error_message="текст по умолчанию - элемент не пропал"):
        wait_result = WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator),
                                                                error_message)
        return wait_result

    def find_element(self, locator):
        locator_type = locator[0]
        print(
            f'#### locator_type is {locator_type} ####')
        locator_value = locator[1]
        print(f'#### locator_value is {locator_value} ####')
        try:
            check_result = self.driver.find_element(locator_type, locator_value)
            return check_result
        except NoSuchElementException:
            print("Элемент не найден")
            return None

    # def find_element(self):
    #     # locator_type = f'AppiumBy.{locator[0].upper()}'
    #     # print(f'#### locator_type is {locator_type} ####')
    #     # locator_value = locator[1]
    #     # print(f'#### locator_value is {locator_value} ####')
    #     check_result = self.driver.find_element(AppiumBy.XPATH,
    #                                             '//android.widget.TextView[@text="Java (programming language)"]')
    #     return check_result
