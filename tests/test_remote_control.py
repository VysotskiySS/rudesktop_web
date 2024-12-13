# file /rudesktop_web/tests/test_remote_control.py

import allure
import pytest
from pages.login_page import LoginPage
from pages.remote_control_page import RemoteControlPage
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
@allure.feature("Удаленный доступ")
class TestRemoteControlPage:

    @pytest.mark.rc
    @pytest.mark.smoke
    @allure.title('Фильтр - Поиск устройства')
    def test_find_device(self):
        login = LoginPage()
        login.login()
        main = MainPage()
        main.open_devices()
        rc = RemoteControlPage()
        # rc.filter_search()

    @pytest.mark.rc
    @pytest.mark.smoke
    @allure.title('Добавить адрес')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=226")
    def test_add_address(self):
        login = LoginPage()
        login.login()
        rc = RemoteControlPage()
        rc.open_address_book()
        main = MainPage()
        main.clear_all_in_list()
        rc.add_address()

    @pytest.mark.rc
    @pytest.mark.smoke
    @allure.title('Удалить адрес')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=228")
    def test_delete_address(self):
        login = LoginPage()
        login.login()
        rc = RemoteControlPage()
        rc.open_address_book()
        main = MainPage()
        main.clear_all_in_list()
        rc.add_address()
        main.delete_element_in_list()

    @pytest.mark.rc
    @pytest.mark.smoke
    @allure.title('Добавить тег')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=227")
    def test_add_teg(self):
        login = LoginPage()
        login.login()
        rc = RemoteControlPage()
        rc.open_tags()
        main = MainPage()
        main.clear_all_in_list()
        rc.add_tag()

    @pytest.mark.rc
    @pytest.mark.smoke
    @allure.title('Удалить тег')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=229")
    def test_delete_teg(self):
        login = LoginPage()
        login.login()
        rc = RemoteControlPage()
        rc.open_tags()
        main = MainPage()
        main.clear_all_in_list()
        rc.add_tag()
        main.delete_element_in_list()

    @pytest.mark.rc
    @pytest.mark.smoke
    @allure.title('Удалить все устройства на странице')
    def test_delete_devices(self):
        login = LoginPage()
        login.login()
        main = MainPage()
        main.open_devices()
        rc = RemoteControlPage()
        main = MainPage()
        main.clear_all_in_list()
