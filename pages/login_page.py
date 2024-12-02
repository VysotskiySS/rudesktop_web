import allure

from pages.base_page import BasePage
from selene.api import be, have, s
from config import *

class LoginPage(BasePage):

    LOGIN_MSG = s('//p[@class="login-box-msg"]')
    PASSWORD_FIELD = s('//input[@id="password"]')
    LOGIN_FIELD = s('//input[@id="username"]')
    METHOD_AUTH = s('//select[@name="domain"]')
    DOMAIN_SELECTOR = s('//option[value="@win2012.local"]')
    LOCAL_SELECTOR = s('//option[value="@Локальный"]')
    SUBMIT_BTN = s('//button[@type="submit"]')
    RESTORE_PASS = s('//a[contains(text(),"Забыли свой пароль или имя пользователя?")]')
    LOGIN_ICON = s('li.nav-item.dropdown')
    LOGO = s('img[alt="RuDesktop"]')
    EMAIL_FIELD = 'input[placeholder="Адрес электронной почты"]'

    @allure.step("Авторизоваться")
    def login(self, login=valid_login_superuser, password=valid_pass):
        self.wait_element(self.LOGO)
        text_msg = self.get_element_text(self.LOGIN_MSG)
        assert text_msg == 'Платформа удаленного администрирования'
        text_btn = self.get_element_text(self.SUBMIT_BTN)
        assert text_btn == 'Войти'
        # Проверить плейсхолдеры
        self.set_text(self.LOGIN_FIELD, login)
        self.set_text(self.PASSWORD_FIELD, password)
        self.click(self.SUBMIT_BTN, 'кнопка [Войти]')
        current_login = self.get_element_text(self.LOGIN_ICON).replace(" ", "")
        assert current_login == login, f'Ожидалось {login} но получено {current_login}'

    @allure.step("Восстановить пароль")
    def reset_pass(self):
        self.wait_element(self.LOGO)
        self.click(self.RESTORE_PASS, 'ссылка [Забыли свой пароль или имя пользователя?]')
        text = self.get_element_text(self.LOGIN_MSG)
        assert text == 'Забыли пароль? Введите свой адрес электронной почты ниже, и мы вышлем вам инструкцию, как установить новый пароль.'
        text_btn = self.get_element_text(self.SUBMIT_BTN)
        assert text_btn == 'Восстановить мой пароль'
        # self.set_text(self.EMAIL_FIELD, valid_email)
        # self.click(self.SUBMIT_BTN, 'кнопка [Восстановить мой пароль]')



