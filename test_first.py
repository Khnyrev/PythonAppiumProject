import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'
TIMEOUT = 5


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

    def wait_for_element(driver, locator, timeout=20, error_message="текст по умолчанию"):
        wait_result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator), error_message)
        return wait_result

    def wait_for_element_and_click(driver, locator, timeout=20, error_message="текст по умолчанию"):
        wait_result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator), error_message)
        return wait_result.click()

    def wait_for_element_and_send_keys(driver, locator, string_value, timeout=20, error_message="текст по умолчанию"):
        wait_result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator), error_message)
        return wait_result.send_keys(string_value)

    # mainpage_search_element = get_driver.find_element(AppiumBy.ID, "search_container")
    # mainpage_search_element.click()
    main_page_search_field_locator = (AppiumBy.ID, "search_container")
    wait_for_element_and_click(get_driver, main_page_search_field_locator, 10)

    search_field_locator = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    wait_for_element_and_send_keys(get_driver, search_field_locator, "PYTHON", 10)

    search_result_locator = (AppiumBy.XPATH,
                             '//android.widget.TextView[@resource-id="org.wikipedia:id/page_list_item_title" and @text="Python (programming language)"]')
    wait_for_element(get_driver, search_result_locator, 15, "Не нашли элемент с локатором: 'search_result_locator'")

    print("SECOND TEST RUUUUN!")
