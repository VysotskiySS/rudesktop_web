# file /rudesktop_web/tests/test_main.py

import allure
import pytest
from pages.login_page import LoginPage
from pages.menu_page import MenuPage

@pytest.mark.usefixtures("setup")
@allure.feature("Меню")
class TestMenuPage:

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Проверка пунктов меню первого уровня')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=212")
    def test_left_menu_l1(self):
        login = LoginPage()
        login.login()
        menu = MenuPage()
        menu.check_left_menu_l1()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Проверка пунктов меню второго уровня')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=212")
    def test_left_menu_l2(self):
        login = LoginPage()
        login.login()
        menu = MenuPage()
        menu.check_left_menu_l2()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Проверка открытия разделов меню')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=212")
    def test_open_pages_menu(self):
        login = LoginPage()
        login.login()
        menu = MenuPage()
        menu.open_pages_menu()
