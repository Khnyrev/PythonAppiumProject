from PythonAppiumProject.pages.main_page_object import Search
from PythonAppiumProject.pages.article_page_object import KebabMenu, SaveArticle, ArticleBody
from PythonAppiumProject.pages.article_list_object import ArticleLists
from PythonAppiumProject.pages.AndroidPages.onbording_page import OnboardingPage
from PythonAppiumProject.pages.base_page import BasePage
import time

""" CHeck search result > 1 and check delete search result"""


def test_search_result(get_driver):

    OnboardingPage(get_driver).skip_onboarding()

    search_results = Search(get_driver)
    search_results.enter_word('PYTHON')

    current_elements_count = search_results.show_search_results('Python')
    few_elements_count = 1  # задаем количество элементов для понятия "несколько" (считаем что 2 это уже несколько)
    # print(f'##### current_elements_count is {current_elements_count} #####')
    assert current_elements_count > few_elements_count, "The number of items is less than expected"
    search_results.clear_search_results()  # clear search field
    current_elements_count = search_results.show_search_results('Python')
    # print(f'##### current_elements_count is {current_elements_count} #####')
    assert current_elements_count < few_elements_count, "The number of items is more than expected"  # Check empty search field


def test_saving_two_articles_in_list(get_driver):
    OnboardingPage(get_driver).skip_onboarding()

    search_results = Search(get_driver)  # почему так???
    search_results.enter_word('PYTHON')
    article_screen = search_results.searched_article('Python (programming language)')
    article_screen.click()  # Open 1st article

    kebab_menu = KebabMenu(get_driver)  # Нормально ли так организовывать следующие 5 строк
    kebab_menu.open_kebab_menu()
    kebab_menu.open_customize_kebab_menu()
    kebab_menu.drug_save_icon()
    base_page = BasePage(get_driver)  # Создаем экземпляр класса BasePage А зачем передавать get_driver?
    base_page.back_to_previous_screen()  # Вызываем метод back_to_previous_screen

    kebab_menu.open_kebab_menu()
    kebab_menu.save_article_kebab_menu()

    save_article_to_list = SaveArticle(get_driver)
    save_article_to_list.add_saved_article_to_list()
    save_article_to_list.set_article_list_name('AAAA')

    save_article_to_list.article_page_search_enter_word('JAVA')
    article_screen = search_results.searched_article('Java (programming language)')
    article_screen.click()  # Open 2nd article

    kebab_menu.open_kebab_menu()
    kebab_menu.save_article_kebab_menu()
    save_article_to_list.add_saved_article_to_list()
    save_article_to_list.add_article_to_existing_list()
    save_article_to_list.view_saved_list()  # здесь происходит нажатие на view saved list

    article_list_element = ArticleLists(get_driver)
    article_list_element.locate_python_element()  # нужно ли передавать сюда элементы(напримерм как в 45й строке) или можно/нужно их хардкодить в описании страницы?
    article_list_element.swipe_element_right()

    article_list_element.check_element_was_deleted()
    article_list_element.check_java_element()

    article_body = ArticleBody(get_driver)
    java_element = article_body.check_java_title()
    java_element.click()
    article_body.check_java_title()


def test_assert_title(get_driver):
    OnboardingPage(get_driver).skip_onboarding()

    search_results = Search(
        get_driver)  # нужно присать каждый раз или нужно создать много функций в файлах page_object ?
    search_results.enter_word('JAVA')
    article_screen = search_results.searched_article('Java (programming language)')
    article_screen.click()

    article_body = ArticleBody(get_driver)
    article_body.check_assert_title()

    time.sleep(5)
