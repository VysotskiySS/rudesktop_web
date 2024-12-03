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
    EMAIL_FIELD = s('input[placeholder="Адрес электронной почты"]')
    MSG_RECOVERY = s('//div[@class="card-body"]')
    LOGOUT_BTN = s('//a[@href="/logout/"]')
    LOGIN_AGAIN_BTN = s('//a[@class="btn btn-primary btn-block"]')

    @allure.step("Авторизоваться")
    def login(self, login=valid_login_superuser, password=valid_pass):
        self.wait_element(self.LOGO)
        text_msg = self.get_element_text(self.LOGIN_MSG)
        assert text_msg == 'Платформа удаленного администрирования'
        text_btn = self.get_element_text(self.SUBMIT_BTN)
        assert text_btn == 'Войти'
        self.assert_placeholder(self.LOGIN_FIELD, 'Логин')
        self.assert_placeholder(self.PASSWORD_FIELD, 'Пароль')
        self.set_text(self.LOGIN_FIELD, login)
        self.set_text(self.PASSWORD_FIELD, password)
        self.click(self.SUBMIT_BTN, 'кнопка [Войти]')
        current_login = self.get_element_text(self.LOGIN_ICON).replace(" ", "")
        assert current_login == login, f'Ожидалось {login} но получено {current_login}'

    def logout(self):
        self.wait_element(self.LOGIN_ICON)
        self.click(self.LOGIN_ICON)
        self.click(self.LOGOUT_BTN)
        self.wait_element(self.LOGO)
        current_text = self.get_element_text(self.LOGIN_MSG)
        assert current_text == 'Платформа удаленного администрирования'
        text_btn = self.get_element_text(self.LOGIN_AGAIN_BTN)
        assert text_btn == 'Войти снова'

    @allure.step("Восстановить пароль")
    def reset_pass(self):
        self.wait_element(self.LOGO)
        self.click(self.RESTORE_PASS, 'ссылка [Забыли свой пароль или имя пользователя?]')
        text = self.get_element_text(self.LOGIN_MSG)
        assert text == 'Забыли пароль? Введите свой адрес электронной почты ниже, и мы вышлем вам инструкцию, как установить новый пароль.'
        self.assert_placeholder(self.EMAIL_FIELD, 'Адрес электронной почты')
        text_btn = self.get_element_text(self.SUBMIT_BTN)
        assert text_btn == 'Восстановить мой пароль'
        self.set_text(self.EMAIL_FIELD, valid_email)
        self.click(self.SUBMIT_BTN, 'кнопка [Восстановить мой пароль]')
        self.wait_element(self.LOGO)
        current_text = self.get_element_text(self.MSG_RECOVERY)
        ref_text_1 = 'Мы отправили вам инструкцию по установке нового пароля на указанный адрес электронной почты (если в нашей базе данных есть такой адрес). Вы должны получить ее в ближайшее время.'
        ref_text_2 = 'Если вы не получили письмо, убедитесь что письмо не попало в спам и был указан правильный электронный адрес.'
        current_text = current_text.split('\n')
        assert current_text[0] == ref_text_1, f'Ожидалось {ref_text_1} но получен {current_text[0]}'
        assert current_text[1] == ref_text_2, f'Ожидалось {ref_text_2} но получен {current_text[1]}'

