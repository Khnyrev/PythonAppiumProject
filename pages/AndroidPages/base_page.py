from appium.webdriver.common.appiumby import AppiumBy
from PythonAppiumProject.SessionStorage import session_storage
from PythonAppiumProject.Utils.element_helpers import wait_for_element, count_searched_elements, clear_search_results


class Basepage:
    LOCATOR_SEARCH_ELEMENT = (AppiumBy.ID, "org.wikipedia:id/search_container")
    LOCATOR_SEARCH_FIELD = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    LOCATOR_ARTICLES_SEARCH_RESULT = (AppiumBy.XPATH, '//android.widget.TextView[starts-with(@resource-id, '
                                                            '"org.wikipedia:id/page_list_item_title") and '
                                                            'starts-with(@text, "{}")]')
    LOCATOR_CLEAR_SEARCH = (AppiumBy.ACCESSIBILITY_ID, 'Clear query')

    def enter_word(self, word):
        search_field_element = wait_for_element(session_storage.get_session(),  # как оптимизировать?
                                                self.LOCATOR_SEARCH_ELEMENT,
                                                10,
                                                'LOCATOR_SEARCH_ELEMENT locator not found')
        search_field_element.click()

        search_field_container = wait_for_element(session_storage.get_session(),
                                                  self.LOCATOR_SEARCH_FIELD,
                                                  10,
                                                  'LOCATOR_SEARCH_FIELD locator not found')
        search_field_container.send_keys(word)

    def check_searched_elements_count_greater_than(self, minimal_count, word):
        self.enter_word(word)
        changed_locator_value = self.LOCATOR_ARTICLES_SEARCH_RESULT[1].format(word)  # добавляем в локатор заданное слово
        locator = (self.LOCATOR_ARTICLES_SEARCH_RESULT[0], changed_locator_value)  # собираем локатор после добавления слова
        # print(f'############################ {locator} ###################################')
        current_elements_count = count_searched_elements(session_storage.get_session(),
                                                         locator,
                                                         10,
                                                         'current_elements_count not found')
        print(f'############################ current_elements_count is {current_elements_count} ###################################')
        assert current_elements_count > minimal_count, "The number of items is less than expected"

    def check_search_result_empty(self):

        current_elements_count = count_searched_elements(session_storage.get_session(),
                                                         self.LOCATOR_ARTICLES_SEARCH_RESULT,
                                                         10,
                                                         'current_elements_count not found')
        print(f'############################ current_elements_count is {current_elements_count} ###################################')
        assert current_elements_count < 1, "The number of items is less than expected"

    def clear_search_field(self):
        clear_search_results(session_storage.get_session(), self.LOCATOR_CLEAR_SEARCH)
