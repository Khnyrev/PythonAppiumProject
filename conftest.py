import pytest
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from PythonAppiumProject.Utils.Platform import get_options

from PythonAppiumProject.SessionStorage import session_storage
from PythonAppiumProject.pages.AndroidPages.onboarding_page import OnboardingPage
from PythonAppiumProject.pages.AndroidPages.base_page import Basepage

from PythonAppiumProject.pages.IOSpages.ios_base_page import IOSBasepage
from PythonAppiumProject.pages.IOSpages.ios_onboarding_page import IOSOnboardingPage
from PythonAppiumProject.pages.IOSpages.ios_saved_page import IOSSavedArticlesPage


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
    # driver = webdriver.Remote("http://host.docker.internal:4723", options=options)  # использовать для запуска в docker
    session_storage.set_session(driver)

    yield
    session_storage.reset_session()


@pytest.fixture()
def onboarding_page():
    platform = os.getenv("PLATFORM")
    if platform == 'android':
        return OnboardingPage()
    else:
        return IOSOnboardingPage()


@pytest.fixture()
def base_page():
    platform = os.getenv("PLATFORM")
    if platform == 'android':
        return Basepage()
    else:
        return IOSBasepage()


@pytest.fixture()
def saved_articles_page():
    platform = os.getenv("PLATFORM")
    if platform == 'android':
        return Basepage()
    else:
        return IOSSavedArticlesPage()
