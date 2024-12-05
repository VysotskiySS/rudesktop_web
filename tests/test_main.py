# file /rudesktop_web/tests/test_main.py

import allure
import pytest

from config import new_pass, valid_pass
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

    @pytest.mark.main
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Открыть страницу профиля пользователя')
    @allure.testcase("")
    def test_open_profile(self):
        login = LoginPage()
        login.login()
        main = MainPage()
        main.open_profile()

    @pytest.mark.main
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Изменить пароль пользователя (невалидные данные)')
    @allure.testcase("")
    def test_change_password_invalid(self):
        login = LoginPage()
        login.login()
        main = MainPage()
        main.invalid_change_password()

    @pytest.mark.main
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Изменить пароль пользователя (валидные данные)')
    @allure.testcase("")
    def test_change_password(self):
        login = LoginPage()
        login.login()
        main = MainPage()
        main.change_password()
        login.logout()
        login.click_enter_again()
        login.login(password=new_pass)
        main.change_password(new_password=valid_pass, old_password=new_pass)