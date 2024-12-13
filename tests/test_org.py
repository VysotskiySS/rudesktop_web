# file /rudesktop_web/tests/test_uem.py

import allure
import pytest
from config import *
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.org_page import OrgPage

@pytest.mark.usefixtures("setup")
@allure.feature("Организация")
class TestOrgPage:

    @pytest.mark.org
    @pytest.mark.smoke
    @allure.title('Добавить домен')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=230")
    def test_add_domain(self):
        login = LoginPage()
        login.login()
        org = OrgPage()
        org.open_domains()
        main = MainPage()
        main.clear_all_in_list()
        org.add_domain()

    @pytest.mark.org
    @pytest.mark.smoke
    @allure.title('Удалить домен')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=231")
    def test_delete_domain(self):
        login = LoginPage()
        login.login()
        org = OrgPage()
        org.open_domains()
        main = MainPage()
        if main.count_element_in_list() == 0:
            org.add_domain()
        main.delete_element_in_list()


