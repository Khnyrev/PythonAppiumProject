import time

from appium.webdriver.common.appiumby import AppiumBy
from PythonAppiumProject.SessionStorage import session_storage
from PythonAppiumProject.Utils.element_helpers import wait_for_element, count_searched_elements, \
    clear_search_results, wait_for_elements


class IOSBasepage:
    LOCATOR_SEARCH_ELEMENT = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSearchField[`name == "Search Wikipedia"`]')
    LOCATOR_SEARCH_FIELD = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSearchField[`name == "Search Wikipedia"`]')
    LOCATOR_ARTICLES_SEARCH_RESULT = (
        AppiumBy.XPATH, '//XCUIElementTypeCell[.//XCUIElementTypeStaticText[contains(@value, "{}")]]')
    # LOCATOR_ARTICLES_SEARCH_RESULT = (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell')
    LOCATOR_CLEAR_SEARCH = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Clear text"`]')
    LOCATOR_SEARCHED_JAVA_ARTICLE = (AppiumBy.IOS_CLASS_CHAIN,
                                     '**/XCUIElementTypeStaticText[`name == "{}"`]')
    # LOCATOR_ARTICLE_SAVE_BUTTON = (AppiumBy.IOS_CLASS_CHAIN, '**//XCUIElementTypeButton[@name="Save for later"]')
    LOCATOR_ARTICLE_SAVE_BUTTON = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Save for later"`]')
    LOCATOR_GOTO_MAIN_BUTTON = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label="W"`]')
    LOCATOR_SAVED_BUTTON = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Saved"`]')
    LOCATOR_EXPLORE_BUTTON = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Explore"`]')

    LOCATOR_ADD_TO_READINGLIST_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "Add")]')

    LOCATOR_SEARCHED_JAVA_ISLAND_ARTICLE = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Java"`]')
    LOCATOR_SEARCHED_JAVASCRIPT_ARTICLE = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == '
                                                                     '"JavaScript"`]')
    LOCATOR_SEARCHED_JAVA_PROGRAM_LANGUAGE_ARTICLE = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name '
                                                                                '== "Java (programming language)"`]')

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

    def check_searched_elements_count_greater_than(self, minimal_count: int, word: str):
        """
            Args:
            minimal_count (int): minimal results count.
            word (str): Search text.

            """
        self.enter_word(word)
        changed_locator_value = self.LOCATOR_ARTICLES_SEARCH_RESULT[1].format(
            word)  # добавляем в локатор заданное слово
        # print(f'############### changed_locator_value is {changed_locator_value} #######################')
        locator = (
            self.LOCATOR_ARTICLES_SEARCH_RESULT[0], changed_locator_value)  # собираем локатор после добавления слова
        # print(f'############################ locator is {locator} ###################################')
        wait_for_element(session_storage.get_session(),
                         locator,
                         10,
                         'не нашли локатор для списка результатов поиска')
        current_elements_count = count_searched_elements(session_storage.get_session(),
                                                         locator,
                                                         10,
                                                         'current_elements_count not found')
        print(
            f'############################ current_elements_count is {current_elements_count} ###################################')
        assert current_elements_count > minimal_count, "The number of items is less than expected"

    def check_search_result_empty(self):
        current_elements_count = count_searched_elements(session_storage.get_session(),
                                                         self.LOCATOR_ARTICLES_SEARCH_RESULT,
                                                         10,
                                                         'current_elements_count not found')
        print(
            f'############################ current_elements_count is {current_elements_count} ###################################')
        assert current_elements_count < 1, "The number of items is less than expected"

    def clear_search_field(self):
        clear_search_results(session_storage.get_session(), self.LOCATOR_CLEAR_SEARCH)

    def open_searched_article(self, word):  # TODO переименовать
        self.enter_word(word)  # ввели слово в строку поиска

        changed_locator_value = self.LOCATOR_SEARCHED_JAVA_ARTICLE[1].format(
            word)  # добавляем в локатор заданное слово
        # print(f'############### changed_locator_value is {changed_locator_value} #######################')

        locator = (
            self.LOCATOR_SEARCHED_JAVA_ARTICLE[0], changed_locator_value)  # собираем локатор после добавления слова
        # print(f'############################ locator is {locator} ###################################')

        searched_article = wait_for_element(session_storage.get_session(),
                                            locator,
                                            10,
                                            'не нашли локатор для списка результатов поиска')

        searched_article.click()

    def click_save_button(self):
        print(self.LOCATOR_ARTICLE_SAVE_BUTTON)
        save_button = wait_for_element(session_storage.get_session(),
                                       self.LOCATOR_ARTICLE_SAVE_BUTTON,
                                       10,
                                       'LOCATOR_ARTICLE_SAVE_BUTTON not found')
        save_button.click()
        time.sleep(5)

    def click_goto_main_screen_button(self):
        main_button = wait_for_element(session_storage.get_session(),
                                       self.LOCATOR_GOTO_MAIN_BUTTON,
                                       10,
                                       'LOCATOR_GOTO_MAIN_BUTTON not found')
        main_button.click()

    def click_saved_articles(self):
        saved_button = wait_for_element(session_storage.get_session(),
                                        self.LOCATOR_SAVED_BUTTON,
                                        10,
                                        'LOCATOR_SAVED_BUTTON not found')
        saved_button.click()

    def click_explore_button(self):
        explore_button = wait_for_element(session_storage.get_session(),
                                          self.LOCATOR_EXPLORE_BUTTON,
                                          10,
                                          'LOCATOR_EXPLORE_BUTTON not found')
        explore_button.click()

    def click_add_to_list(self):
        print(self.LOCATOR_ADD_TO_READINGLIST_BUTTON)
        add_button = wait_for_element(session_storage.get_session(),
                                      self.LOCATOR_ADD_TO_READINGLIST_BUTTON,
                                      10,
                                      'LOCATOR_ADD_TO_READINGLIST_BUTTON not found')
        add_button.click()

    def coordinates_click(
            self):  # пришлось реализовать клик по координатам, так как в билде 690 нет возможновсти получить доступ локаторам на экране статьи
        x_coordinate = 160
        y_coordinate = 740

        # Выполнение клика по заданным координатам
        driver = session_storage.get_session()
        driver.tap([(x_coordinate, y_coordinate)], 1)

    def check_three_results_java_search(self):
        wait_for_element(session_storage.get_session(), self.LOCATOR_SEARCHED_JAVA_PROGRAM_LANGUAGE_ARTICLE,
                         10,
                         'LOCATOR_SEARCHED_JAVA_PROGRAM_LANGUAGE_ARTICLE not found')
        wait_for_element(session_storage.get_session(),
                         self.LOCATOR_SEARCHED_JAVA_ISLAND_ARTICLE,
                         10,
                         'LOCATOR_SEARCHED_JAVA_ISLAND_ARTICLE not found')
        wait_for_element(session_storage.get_session(),
                         self.LOCATOR_SEARCHED_JAVASCRIPT_ARTICLE,
                         10,
                         'LOCATOR_SEARCHED_JAVASCRIPT_ARTICLE not found')
