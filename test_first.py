import pytest
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from .utils import wait_for_element, wait_for_element_and_click, wait_for_element_and_send_keys, \
    wait_for_element_to_disappear, clear_element, assert_element_has_text, count_searched_elements, \
    search_results_check, swipe_up, swipe_up_for_find_element


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

    skip_button_locator = (AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button")
    wait_for_element_and_click(driver, skip_button_locator, 10, "не нашли skip_button_locator")

    yield driver
    driver.quit()


def test_first(get_driver):
    main_page_search_field_locator = (AppiumBy.ID, "search_container")
    wait_for_element_and_click(get_driver, main_page_search_field_locator, 10)

    search_field_locator = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    wait_for_element_and_send_keys(get_driver, search_field_locator, "PYTHON", 10)

    search_result_locator = (AppiumBy.XPATH,
                             '//android.widget.TextView[@resource-id="org.wikipedia:id/page_list_item_title" and @text="Python (programming language)"]')
    wait_for_element(get_driver, search_result_locator, 15, "Не нашли элемент с локатором: 'search_result_locator'")

    print("1st TEST - RUUUUN!")


def test_cancel_search(get_driver):
    main_page_search_field_locator = (AppiumBy.ID, "search_container")
    wait_for_element_and_click(get_driver, main_page_search_field_locator, 10)

    search_field_locator = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    wait_for_element_and_send_keys(get_driver, search_field_locator, "PYTHON", 10)
    clear_element(get_driver, search_field_locator, 10)

    cancel_search_button_locator = (AppiumBy.ACCESSIBILITY_ID, 'Navigate up')
    wait_for_element_and_click(get_driver, cancel_search_button_locator, 10)

    wait_for_element_to_disappear(get_driver, cancel_search_button_locator, 10, 'кнопка присутсвует')

    print("2nd TEST - RUUUUN!")


def test_article_title(get_driver):
    main_page_search_field_locator = (AppiumBy.ID, "search_container")
    wait_for_element_and_click(get_driver, main_page_search_field_locator, 10)

    search_field_locator = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    wait_for_element_and_send_keys(get_driver, search_field_locator, "PYTHON", 10)

    search_result_locator = (AppiumBy.XPATH,
                             '//android.widget.TextView[@resource-id="org.wikipedia:id/page_list_item_title" and @text="Python (programming language)"]')
    wait_for_element_and_click(get_driver, search_result_locator, 10)

    article_title_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="Python (programming language)"]')
    article_title = wait_for_element(get_driver, article_title_locator, 10, "не нашли article_title_locator")
    expected_title = "Python (programming language)"
    assert article_title.text == expected_title, f"Ожидаемый заголовок: '{expected_title}', полученный заголовок: '{article_title.text}'"

    print("3rd TEST - RUUUUN!")


def test_homework_ex2(get_driver):
    home_work_text = "Search Wikipedia2"
    home_work_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="Search Wikipedia"]')
    result = assert_element_has_text(get_driver, home_work_locator, home_work_text, 10)
    assert result, f"Ожидаемый текст ,{home_work_text}'не найден'"

    print("4th TEST - RUUUUN!")


def test_homework_ex3(get_driver):
    main_page_search_field_locator = (AppiumBy.ID, "search_container")
    wait_for_element_and_click(get_driver, main_page_search_field_locator, 10)

    search_field_locator = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    wait_for_element_and_send_keys(get_driver, search_field_locator, "PYTHON", 10)

    search_result_locator = (AppiumBy.XPATH,
                             '//android.widget.TextView[@resource-id="org.wikipedia:id/page_list_item_title" and @text="Python (programming language)"]')
    wait_for_element(get_driver, search_result_locator, 15, "Не нашли элемент с локатором: 'search_result_locator'")

    search_result_locator = (
        '//android.widget.TextView[starts-with(@resource-id, "org.wikipedia:id/page_list_item_title") and starts-with(@text, "Python")] ')
    search_locator_type = AppiumBy.XPATH
    few_elements_count = 1  # задаем количество элементов для понятия "несколько" (считаем что 2 это уже несколько)

    elements_count = count_searched_elements(get_driver, search_result_locator, search_locator_type)
    assert elements_count > few_elements_count, "Количество элементов меньше ожидаемого"

    close_search_button_locator = (AppiumBy.ACCESSIBILITY_ID, 'Clear query')
    wait_for_element_and_click(get_driver, close_search_button_locator, 10)

    elements_count = count_searched_elements(get_driver, search_result_locator, search_locator_type)
    assert elements_count < few_elements_count, "Количество элементов больше ожидаемого"


def test_homework_ex4(get_driver):
    main_page_search_field_locator = (AppiumBy.ID, "search_container")
    wait_for_element_and_click(get_driver, main_page_search_field_locator, 10)

    search_field_locator = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    wait_for_element_and_send_keys(get_driver, search_field_locator, "PYTHON", 10)

    search_results = get_driver.find_elements(AppiumBy.XPATH,
                                              '//android.widget.TextView[@resource-id="org.wikipedia:id/page_list_item_title"]')
    search_key_word = "python"

    assert search_results_check(search_results,
                                search_key_word), "не во всех результатах поиска присутсвует слово 'python'"


def test_swipe(get_driver):
    main_page_search_field_locator = (AppiumBy.ID, "search_container")
    wait_for_element_and_click(get_driver, main_page_search_field_locator, 10)

    search_field_locator = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    wait_for_element_and_send_keys(get_driver, search_field_locator, "PYTHON", 10)

    search_result_locator = (AppiumBy.XPATH,
                             '//android.widget.TextView[@resource-id="org.wikipedia:id/page_list_item_title" and @text="Python (programming language)"]')
    wait_for_element_and_click(get_driver, search_result_locator, 10)

    swipe_up(get_driver, 2000)


def test_swipe_up_for_find_element(get_driver):
    main_page_search_field_locator = (AppiumBy.ID, "search_container")
    wait_for_element_and_click(get_driver, main_page_search_field_locator, 10)

    search_field_locator = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    wait_for_element_and_send_keys(get_driver, search_field_locator, "Appium", 10)

    search_result_locator = (AppiumBy.XPATH,
                             '//android.widget.TextView[@resource-id="org.wikipedia:id/page_list_item_title" and @text="Appium"]')
    wait_for_element_and_click(get_driver, search_result_locator, 10)

    element_locator_type = AppiumBy.ACCESSIBILITY_ID
    element_locator = ('View article in browser')

    swipe_up_for_find_element(get_driver, element_locator_type, element_locator, 2)


def test_save_first_article(get_driver):
    main_page_search_field_locator = (AppiumBy.ID, "search_container")
    wait_for_element_and_click(get_driver, main_page_search_field_locator, 10)

    search_field_locator = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    wait_for_element_and_send_keys(get_driver, search_field_locator, "PYTHON", 10)

    search_result_locator = (AppiumBy.XPATH,
                             '//android.widget.TextView[@resource-id="org.wikipedia:id/page_list_item_title" and @text="Python (programming language)"]')
    wait_for_element_and_click(get_driver, search_result_locator, 10)

    kebab_menu_locator = (AppiumBy.ID, 'org.wikipedia:id/page_toolbar_button_show_overflow_menu')
    wait_for_element_and_click(get_driver, kebab_menu_locator, 10)

    customize_toolbar_locator = (AppiumBy.ID, 'org.wikipedia:id/customize_toolbar')
    wait_for_element_and_click(get_driver, customize_toolbar_locator, 10)
    time.sleep(1)

    wait_for_element(get_driver, (AppiumBy.XPATH,
                                  '//android.widget.TextView[@content-desc="Press and drag an item to reposition it" and @text="Save"]'),
                     10)

    save_icon_dragpoint_locator = get_driver.find_element(AppiumBy.XPATH,
                                                          '(//android.widget.ImageView[@content-desc="Hold the drag icon to move the item"])[1]')
    edit_history_locator = get_driver.find_element(AppiumBy.XPATH,
                                                   '//android.widget.TextView[@content-desc="Press and drag an item to reposition it" and @text="Edit history"]')
    get_driver.drag_and_drop(save_icon_dragpoint_locator, edit_history_locator)

    back_to_previus_button_locator = (AppiumBy.ACCESSIBILITY_ID, 'Navigate up')
    wait_for_element_and_click(get_driver, back_to_previus_button_locator, 10)

    kebab_menu_locator = (AppiumBy.ID, 'org.wikipedia:id/page_toolbar_button_show_overflow_menu')
    wait_for_element_and_click(get_driver, kebab_menu_locator, 10)

    kebab_save_locator = (AppiumBy.ID, 'org.wikipedia:id/page_save')
    wait_for_element_and_click(get_driver, kebab_save_locator, 10)

    add_to_list_locator = (AppiumBy.ID, 'org.wikipedia:id/snackbar_action')
    wait_for_element_and_click(get_driver, add_to_list_locator, 10)

    popup_field_locator = (AppiumBy.ID, 'org.wikipedia:id/text_input_container')
    wait_for_element_and_click(get_driver, popup_field_locator, 10)

    popup_input_field_locator = (AppiumBy.ID, 'org.wikipedia:id/text_input')
    wait_for_element_and_send_keys(get_driver, popup_input_field_locator, 'AAAA', 10)

    popup_ok_locator = (AppiumBy.ID, 'android:id/button1')
    wait_for_element_and_click(get_driver, popup_ok_locator, 10)

    wait_for_element_and_click(get_driver, back_to_previus_button_locator, 10)
    wait_for_element_and_click(get_driver, back_to_previus_button_locator, 10)

    saved_articles_nav_button_locator = (AppiumBy.ID, 'org.wikipedia:id/navigation_bar_item_active_indicator_view')
    wait_for_element_and_click(get_driver, saved_articles_nav_button_locator, 10)

    go_to_article_list_locator = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia:id/navigation_bar_item_small_label_view" and @text="Saved"]')
    wait_for_element_and_click(get_driver, go_to_article_list_locator, 10)

    saved_articles_group_locator = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia:id/item_title" and @text="AAAA"]')
    wait_for_element_and_click(get_driver, saved_articles_group_locator, 10)

    saved_article_locator = get_driver.find_element(AppiumBy.ID, 'org.wikipedia:id/page_list_item_container')

    x_start = 90
    print(f'##### {x_start} x start ######')
    y_start = 960
    print(f'##### {y_start} y start ######')
    x_stop = x_start + 900
    print(f'##### {x_stop} x stop ######')
    y_stop = y_start

    get_driver.swipe(x_start, y_start, x_stop, y_stop, 300)
    time.sleep(10)

    wait_for_element_to_disappear(get_driver, saved_article_locator, 10)
