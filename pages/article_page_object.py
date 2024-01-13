from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from .main_page_object import \
    WikiSearchLocators  # норм ли что экспортировал соседнюю страницу или надо было дублировать здесь?
from appium.webdriver.common.appiumby import AppiumBy


class ArticleScreenLocators:
    LOCATOR_KEBAB_MENU = (AppiumBy.ID, 'org.wikipedia:id/page_toolbar_button_show_overflow_menu')
    LOCATOR_KEBAB_MENU_CUSTOMIZE = (AppiumBy.ID, 'org.wikipedia:id/customize_toolbar')
    LOCATOR_CUSTOMIZE_MENU_SAVE_ICON = (AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Hold the drag '
                                                        'icon to move the item"])[1]')
    LOCATOR_CUSTOMIZE_MENU_EDIT_HISTORY_ICON = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Press and '
                                                                'drag an item to reposition it" and @text="Edit '
                                                                'history"]')
    LOCATOR_KEBAB_MENU_SAVE_ICON = (AppiumBy.ID, 'org.wikipedia:id/page_save')
    LOCATOR_ADD_TO_LIST_BUTTON = (AppiumBy.ID, 'org.wikipedia:id/snackbar_action')
    LOCATOR_SET_ARTICLE_LIST_NAME = (AppiumBy.ID, 'org.wikipedia:id/text_input')
    LOCATOR_ADD_ARTICLE_LIST_CONFIRM_BUTTON = (AppiumBy.ID, 'android:id/button1')
    LOCATOR_ARTICLE_SEARCH_FIELD = (AppiumBy.ID, 'org.wikipedia:id/page_toolbar_button_search')
    LOCATOR_ADD_ARTICLE_TO_EXISTING_LIST = (AppiumBy.ID, 'org.wikipedia:id/item_title')
    LOCATOR_VIEW_LIST_BUTTON = (AppiumBy.ID, 'org.wikipedia:id/snackbar_action')
    LOCATOR_JAVA_ARTICLE_TITLE = (AppiumBy.XPATH,
                                  '//android.widget.TextView[@text="Java (programming language)"]')


class KebabMenu(BasePage):
    def open_kebab_menu(self):
        kebab_menu = self.wait_for_element(ArticleScreenLocators.LOCATOR_KEBAB_MENU)
        return kebab_menu.click()

    def open_customize_kebab_menu(self):
        customize_menu = self.wait_for_element(ArticleScreenLocators.LOCATOR_KEBAB_MENU_CUSTOMIZE)
        return customize_menu.click()

    def drug_save_icon(self):
        draggable_icon = self.wait_for_element(ArticleScreenLocators.LOCATOR_CUSTOMIZE_MENU_SAVE_ICON)
        target_icon = self.wait_for_element(ArticleScreenLocators.LOCATOR_CUSTOMIZE_MENU_EDIT_HISTORY_ICON)
        return self.driver.drag_and_drop(draggable_icon, target_icon)

    def save_article_kebab_menu(self):
        save_kebab_menu = self.wait_for_element(ArticleScreenLocators.LOCATOR_KEBAB_MENU_SAVE_ICON)
        return save_kebab_menu.click()


class SaveArticle(BasePage):

    def add_saved_article_to_list(self):
        add_article = self.wait_for_element(ArticleScreenLocators.LOCATOR_ADD_TO_LIST_BUTTON)
        return add_article.click()

    def set_article_list_name(self, list_name):
        article_list_name = self.wait_for_element(ArticleScreenLocators.LOCATOR_SET_ARTICLE_LIST_NAME)
        article_list_name.send_keys(list_name)
        ok_button = self.wait_for_element(ArticleScreenLocators.LOCATOR_ADD_ARTICLE_LIST_CONFIRM_BUTTON)
        return ok_button.click()

    def article_page_search_enter_word(self, word):
        search_field_element = self.wait_for_element(ArticleScreenLocators.LOCATOR_ARTICLE_SEARCH_FIELD,
                                                     10,
                                                     'can`t found LOCATOR_ARTICLE_SEARCH_FIELD !!!!')
        search_field_element.click()
        search_field_container = self.wait_for_element(WikiSearchLocators.LOCATOR_SEARCH_FIELD,
                                                       10,
                                                       'can`t found LOCATOR_SEARCH_FIELD locator')
        return search_field_container.send_keys(word)

    def add_article_to_existing_list(self):
        add_to_list = self.wait_for_element(ArticleScreenLocators.LOCATOR_ADD_ARTICLE_TO_EXISTING_LIST)
        return add_to_list.click()

    def view_saved_list(self):
        view_list = self.wait_for_element(ArticleScreenLocators.LOCATOR_VIEW_LIST_BUTTON)
        return view_list.click()


class ArticleBody(BasePage):
    def check_java_title(self):
        check_title = self.wait_for_element(ArticleScreenLocators.LOCATOR_JAVA_ARTICLE_TITLE)
        return check_title

    def check_assert_title(self):  # without waiting
        # assert_title = self.find_element(ArticleScreenLocators.LOCATOR_JAVA_ARTICLE_TITLE)
        assert_title = self.find_element(ArticleScreenLocators.LOCATOR_JAVA_ARTICLE_TITLE)
        assert assert_title, 'element JAVA title not found'
