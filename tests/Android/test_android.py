# from PythonAppiumProject.pages.main_page_object import Search
from PythonAppiumProject.pages.article_page_object import KebabMenu, SaveArticle, ArticleBody
from PythonAppiumProject.pages.article_list_object import ArticleLists
from PythonAppiumProject.pages.AndroidPages.onboarding_page import OnboardingPage
from PythonAppiumProject.pages.base_page import BasePage
import time


def test_onboarding_skip(onboarding_page):
    onboarding_page.skip_onboarding_page()


def test_search_result(onboarding_page, base_page):
    onboarding_page.skip_onboarding_page()
    base_page.check_searched_elements_count_greater_than(1, 'Java')
    base_page.clear_search_field()
    base_page.check_search_result_empty()


# def test_saving_two_articles_in_list(get_driver):
#     OnboardingPage(get_driver).skip_onboarding()
#
#     search_results = Search(get_driver)
#     search_results.enter_word('PYTHON')
#     article_screen = search_results.searched_article('Python (programming language)')
#     article_screen.click()  # Open 1st article
#
#     kebab_menu = KebabMenu(get_driver
#     kebab_menu.open_kebab_menu()
#     kebab_menu.open_customize_kebab_menu()
#     kebab_menu.drug_save_icon()
#     base_page = BasePage(get_driver)
#     base_page.back_to_previous_screen()
#
#     kebab_menu.open_kebab_menu()
#     kebab_menu.save_article_kebab_menu()
#
#     save_article_to_list = SaveArticle(get_driver)
#     save_article_to_list.add_saved_article_to_list()
#     save_article_to_list.set_article_list_name('AAAA')
#
#     save_article_to_list.article_page_search_enter_word('JAVA')
#     article_screen = search_results.searched_article('Java (programming language)')
#     article_screen.click()  # Open 2nd article
#
#     kebab_menu.open_kebab_menu()
#     kebab_menu.save_article_kebab_menu()
#     save_article_to_list.add_saved_article_to_list()
#     save_article_to_list.add_article_to_existing_list()
#     save_article_to_list.view_saved_list()  # здесь происходит нажатие на view saved list
#
#     article_list_element = ArticleLists(get_driver)
#     article_list_element.locate_python_element()
#     article_list_element.swipe_element_right()
#
#     article_list_element.check_element_was_deleted()
#     article_list_element.check_java_element()
#
#     article_body = ArticleBody(get_driver)
#     java_element = article_body.check_java_title()
#     java_element.click()
#     article_body.check_java_title()
#
#
# def test_assert_title(get_driver):
#     OnboardingPage(get_driver).skip_onboarding()
#
#     search_results = Search(
#         get_driver)
#     search_results.enter_word('JAVA')
#     article_screen = search_results.searched_article('Java (programming language)')
#     article_screen.click()
#
#     article_body = ArticleBody(get_driver)
#     article_body.check_assert_title()
#
#     time.sleep(5)
