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
    @allure.title('Открыть страницу профиля пользователя')
    @allure.testcase("")
    def test_open_profile(self):
        login = LoginPage()
        login.login()
        main = MainPage()
        main.open_profile()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Изменить пароль пользователя (невалидные данные)')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=219")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=220")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=221")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=222")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=223")
    def test_change_password_invalid(self):
        login = LoginPage()
        login.login()
        main = MainPage()
        main.invalid_change_password()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Изменить пароль пользователя (валидные данные)')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=224")
    def test_change_password(self):
        login = LoginPage()
        login.login(login='auto')
        main = MainPage()
        main.change_password()
        login.logout()
        login.click_enter_again()
        login.login(login='auto')
        login.invalid_login_msg()
        login.login(login='auto', password=new_pass)
        main.change_password(new_password=valid_pass, old_password=new_pass)
