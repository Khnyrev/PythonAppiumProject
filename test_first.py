import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def set_up(request):
    desired_capabilities = dict (
        platformName = "Android",
        deviceName = "AndroidTestDevaice",
        platformVersion = "8.0.0",
        appPackage = "org.wikipedia",
        appActivity = ".main.MainActivity",
        # automationName = "Appium",
        automationName='uiautomator2',
        app = "/Users/alekseykhnyrev/PycharmProjects/PythonAppiumProject/PythonAppiumProject/apks/org.wikipedia.apk"
    )
    # Подключение к Appium серверу
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

    def _tear_down():
        driver.quit()

    request.addfinalizer(_tear_down)
    return driver


def test_first():
    print("FIRST TEST RUUUUN!")
