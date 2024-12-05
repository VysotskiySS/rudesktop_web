# file /rudesktop_web/pages/main_page.py
import allure

from locators import MenuLocators, HeaderLocators, MainLocators
from pages.base_page import BasePage
from selene.api import be, have, s
from config import *

class MainPage(BasePage):





    @allure.step("Проверить наличие пунктов меню")
    def check_left_menu(self):
        l1_menu = [MenuLocators.CONTROL_PANEL, MenuLocators.REMOTE_ACCESS, MenuLocators.MANAGEMENT_UEM, MenuLocators.ORGANIZATION, MenuLocators.AUDIT, MenuLocators.INVENTORY, MenuLocators.REPORTS, MenuLocators.STORAGE, MenuLocators.ADMINISTRATION]
        for menu_item in l1_menu:
            self.wait_element(menu_item)

        self.click(MenuLocators.REMOTE_ACCESS, 'пункт меню [Удаленный доступ]')
        l2_remote_access = [MenuLocators.DEVICES, MenuLocators.SESSIONS, MenuLocators.ADDRESSES, MenuLocators.TAGS]
        for menu_item in l2_remote_access:
            self.wait_element(menu_item)

        self.click(MenuLocators.MANAGEMENT_UEM, 'пункт меню [Управление (UEM)]')
        l2_management_uem = [MenuLocators.POLICIES, MenuLocators.TASKS, MenuLocators.OS_INSTALLATION, MenuLocators.REQUESTS]
        for menu_item in l2_management_uem:
            self.wait_element(menu_item)

        self.click(MenuLocators.ORGANIZATION, 'пункт меню [Организация]')
        l2_organization = [MenuLocators.STRUCTURE, MenuLocators.USERS, MenuLocators.GROUPS, MenuLocators.DOMAINS, MenuLocators.DYNAMIC_GROUPS, MenuLocators.DEPARTMENTS, MenuLocators.INVITATIONS, MenuLocators.NOTIFICATIONS]
        for menu_item in l2_organization:
            self.wait_element(menu_item)

        self.click(MenuLocators.AUDIT, 'пункт меню [Аудит]')
        l2_audit = [MenuLocators.EXECUTION_LOGS, MenuLocators.OBJECTS, MenuLocators.SYSTEM_LOGINS, MenuLocators.HTTP_REQUESTS, MenuLocators.ALL_LOGS]
        for menu_item in l2_audit:
            self.wait_element(menu_item)

        self.click(MenuLocators.INVENTORY, 'пункт меню [Инвентаризация]')
        l2_inventory = [MenuLocators.RESOURCE_AVAILABILITY, MenuLocators.RESOURCE_CATALOG]
        for menu_item in l2_inventory:
            self.wait_element(menu_item)

        self.click(MenuLocators.REPORTS, 'пункт меню [Отчеты]')
        l2_reports = [MenuLocators.TEMPLATES, MenuLocators.PREPARED_REPORTS, MenuLocators.TRENDS, MenuLocators.GRAPH, MenuLocators.MAP]
        for menu_item in l2_reports:
            self.wait_element(menu_item)

        self.click(MenuLocators.STORAGE, 'пункт меню [Хранилище]')
        l2_storage = [MenuLocators.REPOSITORIES, MenuLocators.FILES]
        for menu_item in l2_storage:
            self.wait_element(menu_item)

        self.click(MenuLocators.ADMINISTRATION, 'пункт меню [Администрирование]')
        l2_administration = [MenuLocators.SETTINGS, MenuLocators.KEY_CLOAK, MenuLocators.SUB_NETWORKS, MenuLocators.BRIDGES, MenuLocators.BLACK_LIST, MenuLocators.WHITE_LIST, MenuLocators.CERTIFICATES, MenuLocators.SSH_ACCESS, MenuLocators.KICKSTART, MenuLocators.LICENSE]
        for menu_item in l2_administration:
            self.wait_element(menu_item)

    def open_devices(self):
        self.click(MenuLocators.REMOTE_ACCESS, 'пункт меню [Удаленный доступ]')
        self.click(MenuLocators.DEVICES, 'пункт меню [Устройства]')
        self.assert_active_bread_crumbs('Устройства')

    def open_profile(self):
        self.click(HeaderLocators.LOGIN_ICON)
        self.click(HeaderLocators.PROFILE)
        self.assert_active_bread_crumbs('rude')

    def open_change_pass(self):
        self.click(HeaderLocators.LOGIN_ICON)
        self.click(HeaderLocators.CHANGE_PASSWORD)
        self.assert_active_bread_crumbs('Изменение пароля')

    def invalid_change_password(self, password=new_pass):
        self.open_change_pass()

        self.set_text(MainLocators.OLD_PASSWORD_FIELD, valid_pass)
        self.set_text(MainLocators.NEW_PASSWORD_FIELD, '1234567')
        self.set_text(MainLocators.CONFIRM_NEW_PASSWORD_FIELD, '1234567')
        self.click(MainLocators.CHANGE_PASSWORD_BTN)
        error_msg_text = self.get_element_text(MainLocators.DANGER_MSG)
        assert error_msg_text == 'Пожалуйста исправьте ошибки.'
        error_list = self.get_element_text(MainLocators.ERROR_LIST)
        error_list = self.parse_multiline_string(error_list)
        assert error_list[0] == 'Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.'
        assert error_list[1] == 'Введённый пароль слишком широко распространён.'

        self.set_text(MainLocators.OLD_PASSWORD_FIELD, valid_pass)
        self.set_text(MainLocators.NEW_PASSWORD_FIELD, '12345678')
        self.set_text(MainLocators.CONFIRM_NEW_PASSWORD_FIELD, '12345678')
        self.click(MainLocators.CHANGE_PASSWORD_BTN)
        error_msg_text = self.get_element_text(MainLocators.DANGER_MSG)
        assert error_msg_text == 'Пожалуйста исправьте ошибки.'
        error_list = self.get_element_text(MainLocators.ERROR_LIST)
        error_list = self.parse_multiline_string(error_list)
        assert error_list[0] == 'Введённый пароль слишком широко распространён.'

        self.set_text(MainLocators.OLD_PASSWORD_FIELD, valid_pass)
        self.set_text(MainLocators.NEW_PASSWORD_FIELD, 'S0cut')
        self.set_text(MainLocators.CONFIRM_NEW_PASSWORD_FIELD, 'S0cut')
        self.click(MainLocators.CHANGE_PASSWORD_BTN)
        error_msg_text = self.get_element_text(MainLocators.DANGER_MSG)
        assert error_msg_text == 'Пожалуйста исправьте ошибки.'
        error_list = self.get_element_text(MainLocators.ERROR_LIST)
        error_list = self.parse_multiline_string(error_list)
        assert error_list[0] == 'Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.'

        self.set_text(MainLocators.OLD_PASSWORD_FIELD, valid_pass)
        self.set_text(MainLocators.NEW_PASSWORD_FIELD, password)
        self.set_text(MainLocators.CONFIRM_NEW_PASSWORD_FIELD, 'NewPassw')
        self.click(MainLocators.CHANGE_PASSWORD_BTN)
        error_msg_text = self.get_element_text(MainLocators.DANGER_MSG)
        assert error_msg_text == 'Пожалуйста исправьте ошибки.'
        error_list = self.get_element_text(MainLocators.ERROR_LIST)
        error_list = self.parse_multiline_string(error_list)
        assert error_list[0] == 'Введенные пароли не совпадают.'

    def change_password(self, new_password=new_pass, old_password=valid_pass):
        self.open_change_pass()
        self.set_text(MainLocators.OLD_PASSWORD_FIELD, old_password)
        self.set_text(MainLocators.NEW_PASSWORD_FIELD, new_password)
        self.set_text(MainLocators.CONFIRM_NEW_PASSWORD_FIELD, new_password)
        self.click(MainLocators.CHANGE_PASSWORD_BTN)
        self.wait_element_hidden(MainLocators.DANGER_MSG)
        self.wait_element_hidden(MainLocators.ERROR_LIST)
        success_msg_text = self.get_element_text(MainLocators.SUCCESS_MSG)
        assert success_msg_text == 'Ваш пароль был изменен.'





