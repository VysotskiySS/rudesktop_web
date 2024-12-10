# file /rudesktop_web/pages/main_page.py
import allure
from locators import MenuLocators, HeaderLocators, MainLocators
from pages.base_page import BasePage
from config import *


class MainPage(BasePage):

    @allure.step("Открыть пункт меню [Устройства]")
    def open_devices(self):
        self.click(MenuLocators.REMOTE_ACCESS, 'пункт меню [Удаленный доступ]')
        self.click(MenuLocators.DEVICES, 'пункт меню [Устройства]')
        self.assert_active_bread_crumbs('Устройства')

    @allure.step("Открыть страницу [Профиль]")
    def open_profile(self):
        self.click(HeaderLocators.LOGIN_ICON, 'Иконка [Пользователь]')
        self.click(HeaderLocators.PROFILE, 'кнопка [Профиль]')
        self.assert_active_bread_crumbs('rude')

    def click_change_pass(self):
        self.click(MainLocators.CHANGE_PASSWORD_BTN, 'кнопка [Изменить пароль]')

    @allure.step("Открыть страницу [Изменение пароля]")
    def open_change_pass(self):
        self.click(HeaderLocators.LOGIN_ICON, 'Иконка [Пользователь]')
        self.click(HeaderLocators.CHANGE_PASSWORD, 'кнопка [Изменить пароль]')
        self.assert_active_bread_crumbs('Изменение пароля')

    def invalid_change_password(self, password=new_pass):
        self.open_change_pass()
        with allure.step("Неверный старый пароль"):
            self.set_text(MainLocators.OLD_PASSWORD_FIELD, 'InValidPass')
            self.set_text(MainLocators.NEW_PASSWORD_FIELD, password)
            self.set_text(MainLocators.CONFIRM_NEW_PASSWORD_FIELD, password)
            self.click_change_pass()
            error_msg_text = self.get_element_text(MainLocators.DANGER_MSG)
            assert error_msg_text == 'Пожалуйста исправьте ошибки.'
            error_list = self.get_element_text(MainLocators.ERROR_LIST)
            error_list = self.parse_multiline_string(error_list)
            assert error_list[0] == 'Ваш старый пароль введен неправильно. Пожалуйста, введите его снова.'
        with allure.step("Попытка установить короткий и простой пароль"):
            self.set_text(MainLocators.OLD_PASSWORD_FIELD, valid_pass)
            self.set_text(MainLocators.NEW_PASSWORD_FIELD, '1234567')
            self.set_text(MainLocators.CONFIRM_NEW_PASSWORD_FIELD, '1234567')
            self.click_change_pass()
            error_msg_text = self.get_element_text(MainLocators.DANGER_MSG)
            assert error_msg_text == 'Пожалуйста исправьте ошибки.'
            error_list = self.get_element_text(MainLocators.ERROR_LIST)
            error_list = self.parse_multiline_string(error_list)
            assert error_list[0] == 'Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.'
            assert error_list[1] == 'Введённый пароль слишком широко распространён.'
        with allure.step("Попытка установить простой пароль"):
            self.set_text(MainLocators.OLD_PASSWORD_FIELD, valid_pass)
            self.set_text(MainLocators.NEW_PASSWORD_FIELD, '12345678')
            self.set_text(MainLocators.CONFIRM_NEW_PASSWORD_FIELD, '12345678')
            self.click_change_pass()
            error_msg_text = self.get_element_text(MainLocators.DANGER_MSG)
            assert error_msg_text == 'Пожалуйста исправьте ошибки.'
            error_list = self.get_element_text(MainLocators.ERROR_LIST)
            error_list = self.parse_multiline_string(error_list)
            assert error_list[0] == 'Введённый пароль слишком широко распространён.'
        with allure.step("Попытка установить короткий пароль"):
            self.set_text(MainLocators.OLD_PASSWORD_FIELD, valid_pass)
            self.set_text(MainLocators.NEW_PASSWORD_FIELD, 'S0cut')
            self.set_text(MainLocators.CONFIRM_NEW_PASSWORD_FIELD, 'S0cut')
            self.click_change_pass()
            error_msg_text = self.get_element_text(MainLocators.DANGER_MSG)
            assert error_msg_text == 'Пожалуйста исправьте ошибки.'
            error_list = self.get_element_text(MainLocators.ERROR_LIST)
            error_list = self.parse_multiline_string(error_list)
            assert error_list[0] == 'Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.'
        with allure.step("Пароль и подтверждение пароля не совпадают"):
            self.set_text(MainLocators.OLD_PASSWORD_FIELD, valid_pass)
            self.set_text(MainLocators.NEW_PASSWORD_FIELD, password)
            self.set_text(MainLocators.CONFIRM_NEW_PASSWORD_FIELD, 'NewPassw')
            self.click_change_pass()
            error_msg_text = self.get_element_text(MainLocators.DANGER_MSG)
            assert error_msg_text == 'Пожалуйста исправьте ошибки.'
            error_list = self.get_element_text(MainLocators.ERROR_LIST)
            error_list = self.parse_multiline_string(error_list)
            assert error_list[0] == 'Введенные пароли не совпадают.'


    @allure.step("Изменить пароль")
    def change_password(self, new_password=new_pass, old_password=valid_pass):
        self.open_change_pass()
        self.set_text(MainLocators.OLD_PASSWORD_FIELD, old_password)
        self.set_text(MainLocators.NEW_PASSWORD_FIELD, new_password)
        self.set_text(MainLocators.CONFIRM_NEW_PASSWORD_FIELD, new_password)
        self.click_change_pass()
        self.wait_element_hidden(MainLocators.DANGER_MSG)
        self.wait_element_hidden(MainLocators.ERROR_LIST)
        success_msg_text = self.get_element_text(MainLocators.SUCCESS_MSG)
        assert success_msg_text == 'Ваш пароль был изменен.'





