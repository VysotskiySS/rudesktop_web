# file /rudesktop_web/tests/test_uem.py

import allure
import pytest
from config import *
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.uem_page import UEMPage


@pytest.mark.usefixtures("setup")
@allure.feature("Управление (UEM)")
class TestPolicyPage:

    @pytest.mark.uem
    @pytest.mark.smoke
    @allure.title('Добавить политику')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=234")
    def test_add_policy(self):
        login = LoginPage()
        login.login()
        uem = UEMPage()
        uem.open_policy()
        uem.add_inventory_policy()

    @pytest.mark.uem
    @pytest.mark.smoke
    @allure.title('Удалить политику')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=235")
    def test_delete_policy(self):
        login = LoginPage()
        login.login()
        uem = UEMPage()
        uem.open_policy()
        uem.add_inventory_policy()
        main = MainPage()
        main.delete_element_in_list()

    @pytest.mark.uem
    @pytest.mark.smoke
    @allure.title('Добавить Задачу')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=236")
    def test_add_task(self):
        login = LoginPage()
        login.login()
        uem = UEMPage()
        uem.open_policy()
        main = MainPage()
        if main.count_element_in_list() == 0:
            uem.add_inventory_policy()
        uem.open_tasks()
        uem.add_task()

    @pytest.mark.uem
    @pytest.mark.smoke
    @allure.title('Удалить Задачу')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=237")
    def test_delete_task(self):
        login = LoginPage()
        login.login()
        uem = UEMPage()
        uem.open_tasks()
        main = MainPage()
        if main.count_element_in_list() == 0:
            uem.open_policy(path='cut')
            if main.count_element_in_list() == 0:
                uem.add_inventory_policy()
            uem.open_tasks(path='cut')
            uem.add_task()
        main.delete_element_in_list()