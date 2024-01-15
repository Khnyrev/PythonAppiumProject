from .base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class WikiSearchLocators:
    LOCATOR_SEARCH_ELEMENT = (AppiumBy.ID, "org.wikipedia:id/search_container")
    LOCATOR_SEARCH_FIELD = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    LOCATOR_PYTHON_ARTICLE_SEARCH_RESULT = (AppiumBy.XPATH, '//android.widget.TextView[starts-with(@resource-id, '
                                                            '"org.wikipedia:id/page_list_item_title") and '
                                                            'starts-with(@text, "{}")]')
    # LOCATOR_PYTHON_ARTICLE_SEARCH_RESULT_TYPE = AppiumBy.XPATH

    LOCATOR_SEARCH_RESULTS = (
        '//android.widget.TextView[starts-with(@resource-id, "org.wikipedia:id/page_list_item_title") and '
        'starts-with(@text, "{}")]')
    LOCATOR_SEARCH_RESULT_TYPE = AppiumBy.XPATH

    LOCATOR_CLEAR_SEARCH = (AppiumBy.ACCESSIBILITY_ID, 'Clear query')


class Search(BasePage):
    def enter_word(self, word):
        search_field_element = self.wait_for_element(WikiSearchLocators.LOCATOR_SEARCH_ELEMENT,
                                                     10,
                                                     'can`t found LOCATOR_SEARCH_ELEMENT !!!!')
        search_field_element.click()
        search_field_container = self.wait_for_element(WikiSearchLocators.LOCATOR_SEARCH_FIELD,
                                                       10,
                                                       'can`t found LOCATOR_SEARCH_FIELD locator')
        search_field_container.send_keys(word)
        return search_field_container

    def show_search_results(self, word):
        WikiSearchLocators.LOCATOR_SEARCH_RESULTS = WikiSearchLocators.LOCATOR_SEARCH_RESULTS.format(word)
        current_elements_count = BasePage.count_searched_elements(self, WikiSearchLocators.LOCATOR_SEARCH_RESULTS,
                                                                  WikiSearchLocators.LOCATOR_SEARCH_RESULT_TYPE,
                                                                  10,
                                                                  'can`t found current_elements_count')
        return current_elements_count

    def clear_search_results(self):
        search_field_out_button = self.wait_for_element(WikiSearchLocators.LOCATOR_CLEAR_SEARCH,
                                                        10,
                                                        'can`t found search_field_out_button')
        return search_field_out_button.click()

    def searched_article(self, word):
        updated_locator_python_article_search_result = (
            WikiSearchLocators.LOCATOR_PYTHON_ARTICLE_SEARCH_RESULT[0],
            WikiSearchLocators.LOCATOR_PYTHON_ARTICLE_SEARCH_RESULT[1].replace('"{}"', f'"{word}"'))
        desired_article = self.wait_for_element(updated_locator_python_article_search_result)
        return desired_article
