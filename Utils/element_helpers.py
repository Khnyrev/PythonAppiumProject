from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def pars_locator(locator):
#     locator_type = locator[0]
#     locator_value = locator[1]
#     return locator_type, locator_value


def wait_for_element(driver, locator, timeout=20, error_message="текст по умолчанию"):
    wait_result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator), error_message)
    return wait_result


def count_searched_elements(driver, locator, timeout=20, error_message="текст по умолчанию"):
    # print(f"############## locator is {locator} #######################")
    count_result = driver.find_elements(locator[0], locator[1])
    print(len(count_result))
    return len(count_result)


def clear_search_results(driver, locator):
    search_field_clear_button = wait_for_element(driver,
                                                 locator,
                                                 10,
                                                 f'can`t found search_field_clear_button')
    return search_field_clear_button.click()

# def wait_for_element_and_click(driver, locator, timeout=20, error_message="текст по умолчанию"):
#     wait_result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator), error_message)
#     return wait_result.click()
#
#
# def wait_for_element_and_send_keys(driver, locator, string_value, timeout=20, error_message="текст по умолчанию"):
#     wait_result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator), error_message)
#     return wait_result.send_keys(string_value)
#
#
# def wait_for_element_to_disappear(driver, locator, timeout=20, error_message="текст по умолчанию"):
#     wait_result = WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located(locator), error_message)
#     return wait_result
#
#
# def clear_element(driver, locator, timeout=20, error_message="текст по умолчанию"):
#     clear_result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator), error_message)
#     return clear_result.clear
#
#
# def assert_element_has_text(driver, locator, check_text, error_message="текст по умолчанию", timeout=20):
#     check_result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator), error_message)
#     return check_result.text == check_text
#
#
# def count_searched_elements(driver, locator, locator_type, timeout=20, error_message="текст по умолчанию"):
#     count_result = driver.find_elements(locator_type, locator)
#     print(len(count_result))
#     return len(count_result)
#
#
# def search_results_check(search_results, search_key_word):
#     for result in search_results:
#         if search_key_word in result.text.lower():
#             return True
#     return False
#
#
# def swipe_up(driver, swipe_time):
#     size = driver.get_window_size()
#     start_x = size['width'] / 2
#     start_y = size['height'] * 0.8
#     end_y = size['height'] * 0.4
#     swipe_up_result = driver.swipe(start_x, start_y, start_x, end_y, swipe_time)
#     return swipe_up_result
#
#
# def swipe_up_for_find_element(driver, locator_type, locator, max_swipes):
#     already_swipe = 0
#     while len(driver.find_elements(locator_type, locator)) == 0:
#         if already_swipe > max_swipes:
#             locator_check = (locator_type, locator)
#             wait_for_element(driver, locator_check, 10)
#             return
#         swipe_up(driver, 200)
#         already_swipe += 1
