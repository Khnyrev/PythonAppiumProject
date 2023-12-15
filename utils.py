from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element(driver, locator, timeout=20, error_message="текст по умолчанию"):
    wait_result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator), error_message)
    return wait_result


def wait_for_element_and_click(driver, locator, timeout=20, error_message="текст по умолчанию"):
    wait_result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator), error_message)
    return wait_result.click()


def wait_for_element_and_send_keys(driver, locator, string_value, timeout=20, error_message="текст по умолчанию"):
    wait_result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator), error_message)
    return wait_result.send_keys(string_value)


def wait_for_element_to_disappear(driver, locator, timeout=20, error_message="текст по умолчанию"):
    wait_result = WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located(locator), error_message)
    return wait_result

