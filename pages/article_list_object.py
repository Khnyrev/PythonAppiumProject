from .base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class ArticleListsLocators:
    LOCATOR_AAAA_LIST = (AppiumBy.ID, 'org.wikipedia:id/item_title')
    LOCATOR_PYTHON_ICON = (AppiumBy.ACCESSIBILITY_ID, 'Image: Python (programming language)')
    LOCATOR_JAVA_ICON = (AppiumBy.ACCESSIBILITY_ID, 'Image: Java (programming language)')


class ArticleLists(BasePage):

    def locate_python_element(self):  # нужно ли это делать отдельной функцией и в каком модуле? может в base_page?
        element_coordinates = self.wait_for_element(ArticleListsLocators.LOCATOR_PYTHON_ICON,
                                                    10,
                                                    'can`t found element_coordinates').location
        return element_coordinates

    def swipe_element_right(self):
        coordinates = ArticleLists.locate_python_element(self)

        print(f"location is {coordinates}   #######")
        x_start = coordinates['x']
        print(f'##### {x_start} x start ######')
        y_start = coordinates['y']
        print(f'##### {y_start} y start ######')
        x_stop = x_start + 900
        y_stop = y_start

        return self.driver.swipe(x_start, y_start, x_stop, y_stop, 1300)

    def check_element_was_deleted(self):
        return BasePage.wait_for_element_to_disappear(self, ArticleListsLocators.LOCATOR_PYTHON_ICON, 10,  # почему сюда передаем self ?
                                               'LOCATOR_PYTHON_ICON was found')

    def check_java_element(self):
        java_check_result = self.wait_for_element(ArticleListsLocators.LOCATOR_JAVA_ICON, 10, 'cant`found LOCATOR_JAVA_ICON')
        return java_check_result

