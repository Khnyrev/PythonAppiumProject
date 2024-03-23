import time
import allure


@allure.title("Simple Onboarding skip")
@allure.description("this test just clicks the skip button, it doesn't test anything else.")
def test_onboarding_skip(onboarding_page):
    onboarding_page.skip_onboarding_page()
    # time.sleep(5)


@allure.title("Check search work")
@allure.description("this test checks that the number of articles found for a given word is greater than a given number")
def test_search_result(onboarding_page, base_page):

    onboarding_page.skip_onboarding_page()
    base_page.check_searched_elements_count_greater_than(1, 'Python')
    base_page.clear_search_field()
    base_page.check_search_result_empty()


def test_saving_two_articles_in_list(onboarding_page, base_page, saved_articles_page):
    onboarding_page.skip_onboarding_page()

    base_page.click_saved_articles()
    saved_articles_page.click_reading_lists()
    saved_articles_page.click_create_new_reading_lists()
    saved_articles_page.input_list_tile('Home Work')
    saved_articles_page.click_create_readinglist_button()
    base_page.click_explore_button()

    base_page.open_searched_article('Java (programming language)')
    base_page.click_save_button()
    base_page.coordinates_click()
    saved_articles_page.click_existing_homework_list()
    base_page.click_goto_main_screen_button()

    base_page.open_searched_article('Python (programming language)')
    base_page.click_save_button()
    base_page.coordinates_click()
    saved_articles_page.click_existing_homework_list()
    base_page.click_goto_main_screen_button()

    base_page.click_saved_articles()
    saved_articles_page.click_reading_lists()
    saved_articles_page.click_existing_homework_list()
    saved_articles_page.del_saved_python_article()
    saved_articles_page.check_java_article_in_list()


def test_check_three_search_results(onboarding_page, base_page):
    onboarding_page.skip_onboarding_page()
    base_page.enter_word('Java')
    base_page.check_three_results_java_search()