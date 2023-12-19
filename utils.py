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


def clear_element(driver, locator, timeout=20, error_message="текст по умолчанию"):
    clear_result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator), error_message)
    return clear_result.clear


# Необходимо написать функцию, которая проверяет наличие ожидаемого текста у элемента.
# Предлагается назвать ее assertElementHasText. На вход эта функция должна принимать локатор элемент,
# ожидаемый текст и текст ошибки, который будет написан в случае, если элемент по этому локатору не содержит текст,
# который мы ожидаем.

def assert_element_has_text(driver, locator, check_text, error_message="текст по умолчанию", timeout=20):
    check_result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator), error_message)
    return check_result.text == check_text


def count_searched_elements(driver, locator, locator_type, timeout=20, error_message="текст по умолчанию"):
    count_result = driver.find_elements(locator_type, locator)
    print(len(count_result))
    return len(count_result)
