import pytest
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

from PythonAppiumProject.SessionStorage import session_storage
from PythonAppiumProject.pages.AndroidPages.onboarding_page import OnboardingPage
from PythonAppiumProject.pages.AndroidPages.base_page import Basepage



def pytest_report_header():
    """Благодарность тестеру за выполнение тестов."""
    return "Thanks for running the tests."


APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'
PLATFORM_IOS = 'ios'
PLATFORM_ANDROID = 'android'


@pytest.fixture(autouse=True)
def get_driver(request):
    platform = os.getenv("PLATFORM")
    print(f' ##################### platform is {platform} #####################')
    options = get_options(platform)

    # Подключение к Appium серверу
    driver = webdriver.Remote("http://0.0.0.0:4723", options=options)

    session_storage.set_session(driver)

    yield
    session_storage.reset_session()


@pytest.fixture()
def onboarding_page():
    return OnboardingPage()


@pytest.fixture()
def base_page():
    return Basepage()


def get_options(platform):  # есть ли разница где сохранять этот блок?
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
