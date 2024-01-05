import pytest
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


from PythonAppiumProject.utils import wait_for_element_and_click, wait_for_element_and_send_keys, wait_for_element


def pytest_report_header():
    """Благодарность тестеру за выполнение тестов."""
    return "Thanks for running the tests."


@pytest.fixture
def get_driver(request):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platformVersion = '13.0'
    options.device_name = "some_device"
    options.app_activity = ".main.MainActivity"
    options.app_package = "org.wikipedia"
    options.automation_name = "UiAutomator2"
    options.app = "/Users/alekseykhnyrev/PycharmProjects/PythonAppiumProject/PythonAppiumProject/apks/org.wikipedia.apk"

    # Подключение к Appium серверу
    driver = webdriver.Remote("http://0.0.0.0:4723", options=options)

    skip_button_locator = (AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button")
    wait_for_element_and_click(driver, skip_button_locator, 10, "не нашли skip_button_locator")

    yield driver
    driver.quit()


APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'
