from appium.webdriver.common.appiumby import AppiumBy
from PythonAppiumProject.SessionStorage import session_storage
from PythonAppiumProject.Utils.element_helpers import wait_for_element, count_searched_elements, \
    clear_search_results, wait_for_elements


class IOSSavedArticlesPage:
    LOCATOR_READING_LIST_BUTTON = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Reading lists"`]')
    LOCATOR_CREATE_NEW_LIST_BUTTON = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Create a new '
                                                                'list"`]')
    LOCATOR_READING_LIST_TITLE_FIELD = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "reading '
                                                                  'list title"`]')
    LOCATOR_CREATE_READING_LIST_BUTTON = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Create '
                                                                    'reading list"`]')
    LOCATOR_HOMEWORK_READING_LIST = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Home Work"`]')

    LOCATOR_SAVED_PYTHON_ARTICLE = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow['
                                                              '1]/XCUIElementTypeOther/XCUIElementTypeOther'
                                                              '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                              '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                              '/XCUIElementTypeOther['
                                                              '2]/XCUIElementTypeCollectionView/XCUIElementTypeCell['
                                                              '1]/XCUIElementTypeOther[2]/XCUIElementTypeImage')
    LOCATOR_DELETED_PYTHON_ARTICLE = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "swipe action '
                                                                'delete"`]')
    LOCATOR_JAVA_ARTICLE_IN_LIST = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Java (programming language)"`]')

    def click_reading_lists(self):
        reading_lists = wait_for_element(session_storage.get_session(),
                                         self.LOCATOR_READING_LIST_BUTTON,
                                         10,
                                         'LOCATOR_READING_LIST_BUTTON not found')
        reading_lists.click()

    def click_create_new_reading_lists(self):
        create_reading_lists = wait_for_element(session_storage.get_session(),
                                                self.LOCATOR_CREATE_NEW_LIST_BUTTON,
                                                10,
                                                'LOCATOR_CREATE_NEW_LIST_BUTTON not found')
        create_reading_lists.click()

    def input_list_tile(self, word):
        title_field_element = wait_for_element(session_storage.get_session(),  # как оптимизировать?
                                               self.LOCATOR_READING_LIST_TITLE_FIELD,
                                               10,
                                               'LOCATOR_READING_LIST_TITLE_FIELD locator not found')
        # title_field_element.click()
        #
        # search_field_container = wait_for_element(session_storage.get_session(),
        #                                           self.LOCATOR_SEARCH_FIELD,
        #                                           10,
        #                                           'LOCATOR_SEARCH_FIELD locator not found')
        title_field_element.send_keys(word)

    def click_create_readinglist_button(self):
        create_list_button = wait_for_element(session_storage.get_session(),  # как оптимизировать?
                                              self.LOCATOR_CREATE_READING_LIST_BUTTON,
                                              10,
                                              'LOCATOR_CREATE_READING_LIST_BUTTON locator not found')
        create_list_button.click()

    def click_existing_homework_list(self):
        existing_list = wait_for_element(session_storage.get_session(),
                                         self.LOCATOR_HOMEWORK_READING_LIST,
                                         10,
                                         'LOCATOR_HOMEWORK_READING_LIST not found')
        existing_list.click()

    def del_saved_python_article(self):
        saved_python_article = wait_for_element(session_storage.get_session(),
                                                self.LOCATOR_SAVED_PYTHON_ARTICLE,
                                                10,
                                                'LOCATOR_SAVED_PYTHON_ARTICLE not found')

        coordinates = saved_python_article.location
        print(coordinates)

        x_start = coordinates['x']
        y_start = coordinates['y']
        x_stop = x_start - 900
        y_stop = y_start

        driver = session_storage.get_session()
        driver.swipe(x_start, y_start, x_stop, y_stop, 1300)

        delete_python_article_button = wait_for_element(session_storage.get_session(),
                                                        self.LOCATOR_DELETED_PYTHON_ARTICLE,
                                                        10,
                                                        'not found ')
        delete_python_article_button.click()

    def check_java_article_in_list(self):
        wait_for_element(session_storage.get_session(), self.LOCATOR_JAVA_ARTICLE_IN_LIST, 10,
                         'LOCATOR_JAVA_ARTICLE_IN_LIST not found')
        print('####  УРА ОНА НАКОНЕЦ УДАЛИЛАСЬ!!! ####')