# file /rudesktop_web/pages/uem_page.py
import allure
from locators import *
from pages.base_page import BasePage
import random
from config import *


class UEMPage(BasePage):

    @allure.step("Открыть страницу [Политики]")
    def open_policy(self, path='full'):
        if path == 'full':
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

    @allure.step("Добавить политику [Инвентаризация]")
    def add_inventory_policy(self):
        self.click(UEMLocators.ADD_POLICY_BTN, 'кнопка [Добавить Политику]')
        self.click(UEMLocators.MAINTENANCE_AND_ADMINISTRATION_POLICY, 'пункт [Обслуживание и администрирование]')
        self.click(UEMLocators.INVENTORY, 'пункт [Инвентаризация]')
        self.set_text(UEMLocators.NAME_FIELD, 'Инвентаризация')
        self.click(UEMLocators.SAVE_BTN, 'кнопка [Сохранить]')

    @allure.step("Открыть страницу [Задачи]")
    def open_tasks(self, path='full'):
        if path == 'full':
            self.click(MenuLocators.MANAGEMENT_UEM, 'пункт меню [Управление (UEM)]')
        self.click(MenuLocators.TASKS, 'пункт меню [Задачи]')

    @allure.step("Добавить задачу с случайными политиками")
    def add_task(self):
        self.click(UEMLocators.ADD_TASK_BTN, 'кнопка [Добавить Задачу]')
        self.set_text(UEMLocators.NAME_FIELD, 'Новая задача')
        iterations = random.randint(1, 3)
        for i in range(iterations):
            self.click_random_element(UEMLocators.CHECKBOX_POLICY_LIST)
        self.click(UEMLocators.SAVE_INPUT, 'кнопка [Сохранить]')
        self.wait_element(MainLocators.SUCCESS_ALERT)



