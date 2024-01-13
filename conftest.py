import pytest
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


# from PythonAppiumProject.utils import wait_for_element_and_click, wait_for_element_and_send_keys, wait_for_element


def pytest_report_header():
    """Благодарность тестеру за выполнение тестов."""
    return "Thanks for running the tests."


PLATFORM_IOS = 'ios'
PLATFORM_ANDROID = 'android'


@pytest.fixture(autouse=True)
def get_driver(request):

    check = os.environ.get('PLATFORM')
    print(f' ##################### TRY os.environ.get platform is {check} #####################')


    # print(f' ##################### platform is {platform} #####################')
    # os.environ['PLATFORM'] = 'android-r2d2'

    platform = os.getenv("PLATFORM")
    print(f' ##################### platform is {platform} #####################')
    options = get_options(PLATFORM_ANDROID)
    # Подключение к Appium серверу
    driver = webdriver.Remote("http://0.0.0.0:4723", options=options)

    # skip_button_locator = (AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button")
    # wait_for_element_and_click(driver, skip_button_locator, 10, "не нашли skip_button_locator")

    # skip_button = driver.find_element(AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button")
    # skip_button.click()

    yield driver
    driver.quit()


APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


def get_options(platform):
    if platform == PLATFORM_ANDROID:
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platformVersion = '13.0'
        options.device_name = "some_device"
        options.app_activity = ".main.MainActivity"
        options.app_package = "org.wikipedia"
        options.automation_name = "UiAutomator2"
        options.app = "/Users/alekseykhnyrev/PycharmProjects/PythonAppiumProject/PythonAppiumProject/apks/org.wikipedia.apk"
    elif platform == PLATFORM_IOS:
        options = XCUITestOptions()
        options.platformName = "IOS"
        options.deviceName = "iPhone 15"
        options.platformVersion = "17.0"
        options.app = "/Users/alekseykhnyrev/ios_projects/Wikipedia.app"
        options.automation_name = "XCUITest"
    else:
        raise ValueError("Invalid platform name")
    return options
