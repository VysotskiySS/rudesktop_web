# file /rudesktop_web/pages/menu_page.py
import allure
from locators import MenuLocators, HeaderLocators, MainLocators
from pages.base_page import BasePage
from selene.api import be, have, s
from config import *

class MenuPage(BasePage):


    @allure.step("Проверить наличие пунктов меню первого уровня")
    def check_left_menu_l1(self):
        l1_menu = [MenuLocators.CONTROL_PANEL, MenuLocators.REMOTE_ACCESS, MenuLocators.MANAGEMENT_UEM, MenuLocators.ORGANIZATION, MenuLocators.AUDIT, MenuLocators.INVENTORY, MenuLocators.REPORTS, MenuLocators.STORAGE, MenuLocators.ADMINISTRATION]
        for menu_item in l1_menu:
            self.wait_element(menu_item)

    @allure.step("Проверить наличие пунктов меню второго уровня")
    def check_left_menu_l2(self):
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

    @allure.step("Проверить открытие страниц разделов меню")
    def open_pages_menu(self):
        self.click(MenuLocators.REMOTE_ACCESS, 'пункт меню [Удаленный доступ]')
        values_to_check = {
            MenuLocators.DEVICES: "Устройства",
            MenuLocators.SESSIONS: "Сессии",
            MenuLocators.ADDRESSES: "Адреса",
            MenuLocators.TAGS: "Теги",
            MenuLocators.POLICIES: "Политики",
            MenuLocators.TASKS: "Задачи",
            MenuLocators.OS_INSTALLATION: "Установка OS",
            MenuLocators.REQUESTS: "Обращения",
            # MenuLocators.STRUCTURE: "Структура организации",
            MenuLocators.USERS: "Пользователи",
            MenuLocators.GROUPS: "Группы",
            MenuLocators.DOMAINS: "Домены",
            MenuLocators.DYNAMIC_GROUPS: "Динамические группы",
            MenuLocators.DEPARTMENTS: "Подразделения",
            MenuLocators.INVITATIONS: "Приглашения",
            MenuLocators.NOTIFICATIONS: "Уведомления",
            MenuLocators.EXECUTION_LOGS: "Логи исполнения",
            MenuLocators.OBJECTS: "Объекты",
            MenuLocators.SYSTEM_LOGINS: "Входы в систему",
            MenuLocators.HTTP_REQUESTS: "HTTP запросы",
            MenuLocators.ALL_LOGS: "Все логи",
            MenuLocators.RESOURCE_AVAILABILITY: "Наличие ресурсов",
            MenuLocators.RESOURCE_CATALOG: "Каталог ресурсов",
            MenuLocators.TEMPLATES: "Шаблоны",
            MenuLocators.PREPARED_REPORTS: "Готовые отчеты",
            # MenuLocators.TRENDS: "Тренды",
            # MenuLocators.GRAPH: "Граф сети",
            # MenuLocators.MAP: "Карта",
            MenuLocators.REPOSITORIES:"Репозитории",
            MenuLocators.FILES: "Файлы",
            MenuLocators.SETTINGS: "Настройки",
            MenuLocators.KEY_CLOAK:"KeyCloak",
            MenuLocators.SUB_NETWORKS:"Подсети",
            MenuLocators.BRIDGES:"Мосты",
            MenuLocators.TASK_QUEUE:"Очередь задач",
            MenuLocators.BLACK_LIST:"Черный список",
            MenuLocators.WHITE_LIST:"Белый список",
            MenuLocators.CERTIFICATES:"Cертификаты", # одна буква англ исправить
            MenuLocators.SSH_ACCESS:"Доступы",
            MenuLocators.KICKSTART:"Kickstart",
            # MenuLocators.LICENSE: "",
        }
        l2_remote_access = [MenuLocators.DEVICES, MenuLocators.SESSIONS, MenuLocators.ADDRESSES, MenuLocators.TAGS]
        for menu_item in l2_remote_access:
            self.click(menu_item, f'пункт меню[{values_to_check.get(menu_item, None)}]')
            current_text = self.get_element_text(HeaderLocators.ACTIVE_BREAD_CRUMB)
            assert  current_text == values_to_check.get(menu_item, None)

        self.click(MenuLocators.MANAGEMENT_UEM, 'пункт меню [Управление (UEM)]')
        l2_management_uem = [MenuLocators.POLICIES, MenuLocators.TASKS, MenuLocators.OS_INSTALLATION, MenuLocators.REQUESTS]
        for menu_item in l2_management_uem:
            self.click(menu_item, f'пункт меню[{values_to_check.get(menu_item, None)}]')
            current_text = self.get_element_text(HeaderLocators.ACTIVE_BREAD_CRUMB)
            assert current_text == values_to_check.get(menu_item, None), f'Ожидалось {values_to_check.get(menu_item, None)}, но получено {current_text}'

        self.click(MenuLocators.ORGANIZATION, 'пункт меню [Организация]')
        self.click(MenuLocators.STRUCTURE, 'пункт меню [Структура]')
        current_text = self.get_element_text(s('//li[@class="nav-item d-none d-sm-inline-block"]//li[2]'))
        assert current_text == 'Структура организации'

        l2_organization = [MenuLocators.USERS, MenuLocators.GROUPS, MenuLocators.DOMAINS, MenuLocators.DYNAMIC_GROUPS, MenuLocators.DEPARTMENTS, MenuLocators.INVITATIONS, MenuLocators.NOTIFICATIONS]
        for menu_item in l2_organization:
            self.click(menu_item, f'пункт меню[{values_to_check.get(menu_item, None)}]')
            current_text = self.get_element_text(HeaderLocators.ACTIVE_BREAD_CRUMB)
            assert current_text == values_to_check.get(menu_item, None), f'Ожидалось {values_to_check.get(menu_item, None)}, но получено {current_text}'

        self.click(MenuLocators.AUDIT, 'пункт меню [Аудит]')
        l2_audit = [MenuLocators.EXECUTION_LOGS, MenuLocators.OBJECTS, MenuLocators.SYSTEM_LOGINS, MenuLocators.HTTP_REQUESTS, MenuLocators.ALL_LOGS]
        for menu_item in l2_audit:
            self.click(menu_item, f'пункт меню[{values_to_check.get(menu_item, None)}]')
            current_text = self.get_element_text(HeaderLocators.ACTIVE_BREAD_CRUMB)
            assert current_text == values_to_check.get(menu_item, None), f'Ожидалось {values_to_check.get(menu_item, None)}, но получено {current_text}'

        self.click(MenuLocators.INVENTORY, 'пункт меню [Инвентаризация]')
        l2_inventory = [MenuLocators.RESOURCE_AVAILABILITY, MenuLocators.RESOURCE_CATALOG]
        for menu_item in l2_inventory:
            self.click(menu_item, f'пункт меню[{values_to_check.get(menu_item, None)}]')
            current_text = self.get_element_text(HeaderLocators.ACTIVE_BREAD_CRUMB)
            assert current_text == values_to_check.get(menu_item, None), f'Ожидалось {values_to_check.get(menu_item, None)}, но получено {current_text}'

        self.click(MenuLocators.REPORTS, 'пункт меню [Отчеты]')

        l2_reports = [MenuLocators.TEMPLATES, MenuLocators.PREPARED_REPORTS]
        for menu_item in l2_reports:
            self.click(menu_item, f'пункт меню[{values_to_check.get(menu_item, None)}]')
            current_text = self.get_element_text(HeaderLocators.ACTIVE_BREAD_CRUMB)
            assert current_text == values_to_check.get(menu_item, None), f'Ожидалось {values_to_check.get(menu_item, None)}, но получено {current_text}'

        self.click(MenuLocators.TRENDS, 'пункт меню [Тренды]')
        current_text = self.get_element_text(s('//li[@class="nav-item d-none d-sm-inline-block"]//li[2]'))
        assert current_text == 'Тренды', f'Ожидалось Тренды, но получено {current_text}'

        self.click(MenuLocators.GRAPH, 'пункт меню [Граф]')
        current_text = self.get_element_text(s('//li[@class="nav-item d-none d-sm-inline-block"]//li[2]'))
        assert current_text == 'Граф сети', f'Ожидалось Граф сети, но получено {current_text}'

        self.click(MenuLocators.MAP, 'пункт меню [Карта]')
        current_text = self.get_element_text(s('//li[@class="nav-item d-none d-sm-inline-block"]//li[2]'))
        assert current_text == 'Карта', f'Ожидалось Карта, но получено {current_text}'

        self.click(MenuLocators.STORAGE, 'пункт меню [Хранилище]')
        l2_storage = [MenuLocators.REPOSITORIES, MenuLocators.FILES]
        for menu_item in l2_storage:
            self.click(menu_item, f'пункт меню[{values_to_check.get(menu_item, None)}]')
            current_text = self.get_element_text(HeaderLocators.ACTIVE_BREAD_CRUMB)
            assert current_text == values_to_check.get(menu_item, None), f'Ожидалось {values_to_check.get(menu_item, None)}, но получено {current_text}'

        self.click(MenuLocators.ADMINISTRATION, 'пункт меню [Администрирование]')

        l2_administration = [MenuLocators.SETTINGS, MenuLocators.KEY_CLOAK, MenuLocators.SUB_NETWORKS, MenuLocators.BRIDGES, MenuLocators.TASK_QUEUE, MenuLocators.BLACK_LIST, MenuLocators.WHITE_LIST, MenuLocators.CERTIFICATES, MenuLocators.SSH_ACCESS]
        for menu_item in l2_administration:
            self.click(menu_item, f'пункт меню[{values_to_check.get(menu_item, None)}]')
            current_text = self.get_element_text(HeaderLocators.ACTIVE_BREAD_CRUMB)
            assert current_text == values_to_check.get(menu_item, None), f'Ожидалось {values_to_check.get(menu_item, None)}, но получено {current_text}'

        self.click(MenuLocators.KICKSTART, 'пункт меню [Kickstart]')
        current_text = self.get_element_text(s('//li[@class="nav-item d-none d-sm-inline-block"]//li[2]'))
        assert current_text == 'Kickstart', f'Ожидалось Kickstart, но получено {current_text}'

        self.click(MenuLocators.LICENSE, 'пункт меню [Лицензия]')
        self.wait_element(s('//h1[contains(text(),"Информация о лицензии")]'))
