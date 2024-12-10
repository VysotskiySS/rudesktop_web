import allure
from locators import MainLocators, MenuLocators, RemoteAccessLocators, HeaderLocators
from pages.base_page import BasePage
from selene.api import be, have, s
from config import *


class RemoteControlPage(BasePage):

    @allure.step("Выполнить поиск по ID")
    def filter_search(self):
        count_device_in_list = self.search_same_elements(RemoteAccessLocators.CHECK_BOX_DEVICE_IN_LIST)
        self.set_text(RemoteAccessLocators.FILTER_SEARCH_FIELD, '000111333')
        self.click(RemoteAccessLocators.FIND_BTN, 'кнопка [Найти]')
        self.search_same_elements(RemoteAccessLocators.CHECK_BOX_DEVICE_IN_LIST)
        self.get_attribute(RemoteAccessLocators.ACTION_COUNTER, "data-actions-icnt")
        count_device_in_list_after_search = self.get_attribute(RemoteAccessLocators.ACTION_COUNTER, "data-actions-icnt")

    @allure.step("Открыть адресную книгу")
    def open_address_book(self):
        self.click(MenuLocators.REMOTE_ACCESS)
        self.wait_element(MenuLocators.ADDRESSES)
        self.click(MenuLocators.ADDRESSES)
        self.wait_element(HeaderLocators.ACTIVE_BREAD_CRUMB)
        self.assert_active_bread_crumbs('Адреса')

    @allure.step("Добавить адрес в адресную книгу")
    def add_address(self):
        self.click(RemoteAccessLocators.ADD_ADDRESS)
        self.assert_active_bread_crumbs('Добавить Адрес')
        self.set_text(RemoteAccessLocators.ID_FIELD, '000111333')
        self.set_text(RemoteAccessLocators.NAME_FIELD, 'Alias')
        self.click(RemoteAccessLocators.SAVE_BTN)
        self.wait_element(MainLocators.SUCCESS_ALERT)

    @allure.step("Открыть Теги")
    def open_tags(self):
        self.click(MenuLocators.REMOTE_ACCESS)
        self.wait_element(MenuLocators.TAGS)
        self.click(MenuLocators.TAGS)
        self.wait_element(HeaderLocators.ACTIVE_BREAD_CRUMB)
        self.assert_active_bread_crumbs('Теги')

    @allure.step("Добавить тег")
    def add_tag(self):
        self.click(RemoteAccessLocators.ADD_TAG, 'кнопка [Добавить тег]')
        self.assert_active_bread_crumbs('Добавить Тег')
        self.set_text(RemoteAccessLocators.NAME_TAG_FIELD, 'Tag-1')
        self.click(RemoteAccessLocators.SAVE_BTN, 'кнопка [Сохранить]')
        self.wait_element(MainLocators.SUCCESS_ALERT)

    @allure.step("Получить количество записей в списке")
    def count_element_in_list(self):
        try:
            count = int(self.get_attribute(RemoteAccessLocators.ACTION_COUNTER, "data-actions-icnt"))
            return count
        except:
            count = 0
            return count

    @allure.step("Удалить все элементы из списка на странице")
    def clear_all_in_list(self):
        if self.count_element_in_list() > 0:
            self.click(RemoteAccessLocators.MAIN_CHECK_BOX, 'чекбокс группы элементов')
            self.click(RemoteAccessLocators.SELECTOR, 'селектор [Действия с выбранными объектами]')
            self.click(RemoteAccessLocators.DELETE_SELECTED, 'опция селектора [Удалить выбранные устройства]')
            self.click(RemoteAccessLocators.EXECUTE_BTN, 'кнопка [Выполнить]')
            self.click(RemoteAccessLocators.SUBMIT_BTN, 'кнопка [Да, я уверен]')
            self.wait_element(MainLocators.SUCCESS_ALERT)




