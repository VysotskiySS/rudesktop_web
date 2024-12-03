# file /rudesktop_web/tests/test_main_page.py

import allure
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage

@pytest.mark.usefixtures("setup")
@allure.feature("Главная страница")
class TestMainPage:

    @pytest.mark.main
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Проверка пунктов меню')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=212")
    def test_left_menu(self):
        login = LoginPage()
        login.login()
        main = MainPage()
        main.check_left_menu()
