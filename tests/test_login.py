# file /rudesktop_web/tests/test_login.py

import allure
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
@allure.feature("Авторизация")
class TestLoginPage:

    @pytest.mark.login
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Авторизоваться под локальной учетной записью')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=208")
    def test_local_login(self):
        page = LoginPage()
        page.login()

    @pytest.mark.login
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Выход из учетной записи')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=213")
    def test_logout(self):
        page = LoginPage()
        page.login()
        page.logout()

    @pytest.mark.login
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Форма восстановления пароля')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=211")
    def test_reset_pass(self):
        page = LoginPage()
        page.reset_pass()






