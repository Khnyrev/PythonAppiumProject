import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from .utils import wait_for_element, wait_for_element_and_click, wait_for_element_and_send_keys, wait_for_element_to_disappear


# APPIUM_PORT = 4723
# APPIUM_HOST = '127.0.0.1'
# TIMEOUT = 5


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

    yield driver
    driver.quit()


def test_first(get_driver):
    import time

    main_page_search_field_locator = (AppiumBy.ID, "search_container")
    wait_for_element_and_click(get_driver, main_page_search_field_locator, 10)

    search_field_locator = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    wait_for_element_and_send_keys(get_driver, search_field_locator, "PYTHON", 10)

    search_result_locator = (AppiumBy.XPATH,
                             '//android.widget.TextView[@resource-id="org.wikipedia:id/page_list_item_title" and @text="Python (programming language)"]')
    wait_for_element(get_driver, search_result_locator, 15, "Не нашли элемент с локатором: 'search_result_locator'")

    print("FIRST TEST RUUUUN!")


def test_cancel_search(get_driver):
    main_page_search_field_locator = (AppiumBy.ID, "search_container")
    wait_for_element_and_click(get_driver, main_page_search_field_locator, 10)

    cancel_search_button_locator = (AppiumBy.ID, 'org.wikipedia:id/search_close_btn')
    wait_for_element_and_click(get_driver, cancel_search_button_locator, 10)

    wait_for_element_to_disappear(get_driver, cancel_search_button_locator, 10, 'кнопка присутсвует')

    print("SECOND TEST RUUUUN!")
