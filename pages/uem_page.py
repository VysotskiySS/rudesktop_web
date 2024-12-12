# file /rudesktop_web/pages/uem_page.py
import allure
from locators import *
from pages.base_page import BasePage
from config import *


class UEMPage(BasePage):

    @allure.step("Открыть страницу [Политики]")
    def open_policy(self):
        self.click(MenuLocators.MANAGEMENT_UEM, 'пункт меню [Управление (UEM)]')
        self.click(MenuLocators.POLICIES, 'пункт меню [Политики]')

    @allure.step("Открыть случайную группу из списка политик")
    def open_random_accordion_group_policy(self):
        element = self.get_random_element_from_list(UEMLocators.POLICY_GROUPS_LIST)
        self.click(element, 'случайный элемент из списка категорий политик')

    @allure.step("Добавить новую случайную политику")
    def add_random_policy(self):
        self.click(UEMLocators.ADD_POLICY_BTN, 'кнопка [Добавить Политику]')
        self.open_random_accordion_group_policy()
        # дописать выбор элемента из раскрывающегося списка и т.д.

    def add_inventory_policy(self):
        self.click(UEMLocators.ADD_POLICY_BTN, 'кнопка [Добавить Политику]')
        self.click(UEMLocators.MAINTENANCE_AND_ADMINISTRATION_POLICY, 'пункт [Обслуживание и администрирование]')
        self.click(UEMLocators.INVENTORY, 'пункт [Инвентаризация]')
        self.set_text(UEMLocators.NAME_FIELD, 'Инвентаризация')
        self.click(UEMLocators.SAVE_BTN, 'кнопка [Сохранить]')




