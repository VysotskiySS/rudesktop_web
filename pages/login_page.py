import allure

from locators import LoginLocators, MainLocators
from pages.base_page import BasePage
from selene.api import be, have, s
from config import *

class LoginPage(BasePage):

    @allure.step("Авторизоваться")
    def check_login(self, login=valid_login_superuser, password=valid_pass):
        self.wait_element(LoginLocators.LOGO)
        text_msg = self.get_element_text(LoginLocators.LOGIN_MSG)
        assert text_msg == 'Платформа удаленного администрирования'
        text_btn = self.get_element_text(LoginLocators.SUBMIT_BTN)
        assert text_btn == 'Войти'
        self.assert_placeholder(LoginLocators.LOGIN_FIELD, 'Логин')
        self.assert_placeholder(LoginLocators.PASSWORD_FIELD, 'Пароль')
        self.login()
        current_login = self.get_element_text(LoginLocators.LOGIN_ICON).replace(" ", "")
        assert current_login == login, f'Ожидалось {login} но получено {current_login}'

    @allure.step("Авторизоваться")
    def login(self, login=valid_login_superuser, password=valid_pass):
        self.set_text(LoginLocators.LOGIN_FIELD, login)
        self.set_text(LoginLocators.PASSWORD_FIELD, password)
        self.click(LoginLocators.SUBMIT_BTN, 'кнопка [Войти]')

    def invalid_login_msg(self):
        print('реализовать проверку сообщения при вводе невалидных данных при авторизации')
        current_msg = self.get_element_text(MainLocators.DANGER_MSG)


    @allure.step("Выйти из учетной записи пользователя")
    def logout(self):
        self.wait_element(LoginLocators.LOGIN_ICON)
        self.click(LoginLocators.LOGIN_ICON, 'иконка пользователя в верхнем правом углу')
        self.click(LoginLocators.LOGOUT_BTN, 'кнопка [Выйти]')
        self.wait_element(LoginLocators.LOGO)
        current_text = self.get_element_text(LoginLocators.LOGIN_MSG)
        assert current_text == 'Платформа удаленного администрирования'
        text_btn = self.get_element_text(LoginLocators.LOGIN_AGAIN_BTN)
        assert text_btn == 'Войти снова'

    @allure.step("Восстановить пароль")
    def reset_pass(self):
        self.wait_element(LoginLocators.LOGO)
        self.click(LoginLocators.RESTORE_PASS, 'ссылка [Забыли свой пароль или имя пользователя?]')
        text = self.get_element_text(LoginLocators.LOGIN_MSG)
        assert text == 'Забыли пароль? Введите свой адрес электронной почты ниже, и мы вышлем вам инструкцию, как установить новый пароль.'
        self.assert_placeholder(LoginLocators.EMAIL_FIELD, 'Адрес электронной почты')
        text_btn = self.get_element_text(LoginLocators.SUBMIT_BTN)
        assert text_btn == 'Восстановить мой пароль'
        self.set_text(LoginLocators.EMAIL_FIELD, valid_email)
        self.click(LoginLocators.SUBMIT_BTN, 'кнопка [Восстановить мой пароль]')
        self.wait_element(LoginLocators.LOGO)
        current_text = self.get_element_text(LoginLocators.MSG_RECOVERY)
        ref_text_1 = 'Мы отправили вам инструкцию по установке нового пароля на указанный адрес электронной почты (если в нашей базе данных есть такой адрес). Вы должны получить ее в ближайшее время.'
        ref_text_2 = 'Если вы не получили письмо, убедитесь что письмо не попало в спам и был указан правильный электронный адрес.'
        current_text = current_text.split('\n')
        assert current_text[0] == ref_text_1, f'Ожидалось {ref_text_1} но получен {current_text[0]}'
        assert current_text[1] == ref_text_2, f'Ожидалось {ref_text_2} но получен {current_text[1]}'

    def click_enter_again(self):
        self.click(LoginLocators.ENTER_AGAIN_BTN, 'кнопка [Войти снова]')

