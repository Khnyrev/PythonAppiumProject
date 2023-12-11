import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def set_up(request):
    desired_capabilities = {
        "platformName": "Android",
        "appium:deviceName": "AndroidTestDevaice",
        "appium:platformVersion": "13.0",
        "appium:appPackage": "org.wikipedia",
        "appium:appActivity": ".main.MainActivity",
        "appium:automationName": "UiAutomator2",
        "app": "/Users/alekseykhnyrev/PycharmProjects/PythonAppiumProject/PythonAppiumProject/apks/org.wikipedia.apk"
    }
    # Подключение к Appium серверу
    driver = webdriver.Remote("http://localhost:4723/", desired_capabilities)

    def _tear_down():
        driver.quit()

    request.addfinalizer(_tear_down)
    return driver


def test_first():
    print("FIRST TEST RUUUUN!")
