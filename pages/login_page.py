import time

import allure
from selene import browser

from locators import LoginLocators, MainLocators
from pages.base_page import BasePage
from selene.api import be, have, s
from config import *
import re
from selenium import webdriver

from pages.main_page import MainPage


class LoginPage(BasePage):
    main = MainPage()

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

    @allure.step("Проверка сообщения при вводе невалидных данных на странице авторизации")
    def invalid_login_msg(self):
        current_text = self.get_element_text(MainLocators.DANGER_MSG)
        reference_text = 'Введенные учетные данные недействительны. Убедитесь, что вы правильно ввели имя пользователя и пароль, и повторите попытку.'
        assert current_text == reference_text, f'Ожидалось сообщение {reference_text}, но получено {current_text}'

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

    def open_link_from_mail(self, user_name):
        browser.driver.get(f"https://www.mailforspam.com/mail/{user_name}/1")
        self.open_unsafe()
        message = s("//p[@id='messagebody']")
        self.wait_element(message)
        text = self.get_element_text(message)
        text = self.parse_multiline_string(text)
        value = text[4]
        browser.driver.get(value)

    def extract_username(self, email):
        username = email.split('@')[0]
        return username

    def assert_login_msg(self, reference_msg):
        current_msg = self.get_element_text(LoginLocators.LOGIN_MSG)
        assert current_msg == reference_msg, f'Ожидалось сообщение {reference_msg}, но получено {current_msg}'

    def create_new_user(self):
        self.click(LoginLocators.CREATE_USER, 'ссылка [Создать учетную запись]')
        self.wait_element(LoginLocators.LOGO)
        name = self.generate_random_name()
        self.set_text(LoginLocators.LOGIN_FIELD, name)
        email = self.generate_random_email()
        self.set_text(LoginLocators.EMAIL_FIELD, email)
        full_name = self.generate_random_full_name()
        self.set_text(LoginLocators.FULL_NAME_FIELD, full_name)
        self.set_text(LoginLocators.PHONE_FIELD, '+79896662233')
        self.set_text(LoginLocators.REG_PASSWORD_FIELD, valid_pass)
        self.set_text(LoginLocators.REG_PASSWORD_CONFIRM, valid_pass)

        self.assert_login_msg('Платформа удаленного администрирования')

        self.wait_element(s('//li[contains(text(),"Пароль не должен быть слишком похож на другую вашу личную информацию.")]'))
        self.wait_element(s('//li[contains(text(),"Ваш пароль должен содержать как минимум 8 символов.")]'))
        self.wait_element(s('//li[contains(text(),"Пароль не должен быть слишком простым и распространенным.")]'))
        self.wait_element(LoginLocators.I_HAVE_PROFILE)
        self.click(LoginLocators.REGISTRATION_BTN, 'кнопка [Зарегистрироваться]')

        self.wait_element(LoginLocators.LOGO)
        self.wait_element(s('//p[contains(text(),"Мы отправили вам инструкцию для активации учетной записи на E-Mail.")]'))
        self.wait_element(s('//p[contains(text(),"Если вы не получили письмо, убедитесь что письмо не попало в спам и был указан правильный электронный адрес.")]'))

        # Открыть почту / открыть письмо / получить ссылку
        user_mail = self.extract_username(email)
        time.sleep(10)
        self.open_link_from_mail(user_mail)

        self.wait_element(LoginLocators.LOGO)
        self.assert_login_msg('Регистрация завершена. Вы можете войти в систему.')
        self.click(LoginLocators.ENTER_BTN)

        self.login(login=name, password=valid_pass)
        current_full_name = self.get_element_text(LoginLocators.LOGIN_ICON)
        assert current_full_name == full_name, f'Ожидалось имя пользователя {full_name}, но получено {current_full_name}'
        # main.open_profile()
        # открыть профиль сверить данные





