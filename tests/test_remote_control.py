# file /rudesktop_web/tests/test_remote_control.py

import allure
import pytest

from pages.login_page import LoginPage
from pages.remote_control_page import RemoteControlPage
from pages.main_page import MainPage

@pytest.mark.usefixtures("setup")
@allure.feature("Удаленный доступ")
class TestRemoteControlPage:

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Фильтр - Поиск устройства')
    def test_find_device(self):
        login = LoginPage()
        login.login()
        main = MainPage()
        main.open_devices()
        rc = RemoteControlPage()
        # rc.filter_search()

