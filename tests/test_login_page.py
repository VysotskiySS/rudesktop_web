import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLoginPage:

    def test_superuser_login(self):
        print('debug')



