# PythonAppiumProject

запустить андроид эмулятор `emulator @and130` (изначально требует настройки в android studio)

запустить Appium server `appium` (требует изначальной установки)

запуск тестов: pytest --alluredir=allure-results/ tests/IOS/test_ios.py::test_onboarding_skip tests/IOS/test_ios.py::test_search_result
посмотреть отчет:  allure serve allure-results/
