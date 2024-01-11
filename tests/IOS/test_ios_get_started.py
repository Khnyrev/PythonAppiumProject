# Python/Pytest
import pytest
import time

from appium.options.ios import XCUITestOptions
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from PythonAppiumProject.pages.base_page import BasePage

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'

#
# @pytest.fixture
# def create_ios_driver(custom_opts=None):
#     options = XCUITestOptions()
#     options.platformName = "IOS"
#     options.deviceName = "iPhone 15"
#     options.platformVersion = "17.0"
#     options.app = "/Users/alekseykhnyrev/ios_projects/Wikipedia.app"
#     options.automation_name = "XCUITest"
#     driver = webdriver.Remote("http://0.0.0.0:4723", options=options)
#
#     yield driver
#     driver.quit()


def test_ios_click(get_driver):
    driver = get_driver
    el = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Next"]')
    # el = driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Learn more about Wikipedia"]')
    el.click()
    el.click()
    el.click()

    some_result = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Get started"]')
    some_result.click()
    print('/n### START SLEEPING')
    time.sleep(5)
    print('/n ### STOP SLEEPING ###')
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'wikipedia')
    print('/n#### "ЭВРИКА!!!!! ####"')
    time.sleep(5)
