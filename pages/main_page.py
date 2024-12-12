# file /rudesktop_web/pages/main_page.py
import allure
from locators import MenuLocators, HeaderLocators, MainLocators
from pages.base_page import BasePage
from config import *

# from pages.login_page import LoginPage
# from pages.menu_page import MenuPage
# from pages.org_page import OrgPage
# from pages.remote_control_page import RemoteControlPage
# from pages.uem_page import UEMPage

class MainPage(BasePage):
    # login = LoginPage()
    # menu = MenuPage()
    # org = OrgPage()
    # rc = RemoteControlPage()
    # uem = UEMPage()

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

    @allure.step("Проверить отображение ошибок при невалидных вариантах пароля")
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

    @allure.step("Удалить все элементы из списка на странице")
    def clear_all_in_list(self):
        if self.count_element_in_list() > 0:
            self.click(MainLocators.MAIN_CHECK_BOX, 'чекбокс группы элементов')
            self.click(MainLocators.SELECTOR, 'селектор [Действия с выбранными объектами]')
            self.click(MainLocators.DELETE_SELECTED, 'опция селектора [Удалить выбранные]')
            self.click(MainLocators.EXECUTE_BTN, 'кнопка [Выполнить]')
            self.click_btn_yes_i_am_sure()
            self.wait_element(MainLocators.SUCCESS_ALERT)

    @allure.step("Удалить элемент из списка")
    def delete_element_in_list(self):
        self.click(MainLocators.MORE_OPTION_BTN, 'кнопка [...]')
        self.click(MainLocators.OPTION_DELETE, 'пункт [Удалить] в списке опций')
        count_string = self.get_element_text(MainLocators.COUNT_ELEMENTS)
        count = self.get_int_from_str(count_string)
        assert count == 1, f'На удаление отмечено {count} элементов, ожидался - 1'
        self.click_btn_yes_i_am_sure()
        self.wait_element(MainLocators.SUCCESS_ALERT)

    def click_btn_yes_i_am_sure(self):
        self.click(MainLocators.SUBMIT_BTN, 'кнопка [Да, я уверен]')

    @allure.step("Получить количество записей в списке")
    def count_element_in_list(self):
        try:
            count = int(self.get_attribute(MainLocators.ACTION_COUNTER, "data-actions-icnt"))
            return count
        except:
            count = 0
            return count
