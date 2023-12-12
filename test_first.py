import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


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
    time.sleep(5)
    print("FIRST TEST RUUUUN!")
