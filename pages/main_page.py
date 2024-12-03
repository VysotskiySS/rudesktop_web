# file /rudesktop_web/pages/main_page.py
import allure

from pages.base_page import BasePage
from selene.api import be, have, s
from config import *

class MainPage(BasePage):
    # LEFT_MENU_L1
    CONTROL_PANEL = s('//p[contains(text(),"Панель управления")]')
    REMOTE_ACCESS = s('//a[@class="nav-link"]/p[contains(text(),"Удаленный доступ")]')
    MANAGEMENT_UEM = s('//a[@class="nav-link"]/p[contains(text(),"Управление (UEM)")]')
    ORGANIZATION = s('//a[@class="nav-link"]/p[contains(text(),"Организация")]')
    AUDIT = s('//a[@class="nav-link"]/p[contains(text(),"Аудит")]')
    INVENTORY = s('//a[@class="nav-link"]/p[contains(text(),"Инвентаризация")]')
    REPORTS = s('//a[@class="nav-link"]/p[contains(text(),"Отчеты")]')
    STORAGE = s('//a[@class="nav-link"]/p[contains(text(),"Хранилище")]')
    ADMINISTRATION = s('//a[@class="nav-link"]/p[contains(text(),"Администрирование")]')

    # REMOTE_ACCESS
    DEVICES = s('//a[@class="nav-link"]/p[contains(text(),"Устройства")]')
    SESSIONS = s('//a[@class="nav-link"]/p[contains(text(),"Сессии")]')
    ADDRESSES = s('//a[@class="nav-link"]/p[contains(text(),"Адреса")]')
    TAGS = s('//a[@class="nav-link"]/p[contains(text(),"Теги")]')
    # MANAGEMENT_UEM
    POLICIES = s('//a[@class="nav-link"]/p[contains(text(),"Политики")]')
    TASKS = s('//a[@class="nav-link"]/p[contains(text(),"Задачи")]')
    OS_INSTALLATION = s('//a[@class="nav-link"]/p[contains(text(),"Установка OS")]')
    REQUESTS = s('//a[@class="nav-link"]/p[contains(text(),"Обращения")]')
    # ORGANIZATION
    STRUCTURE = s('//a[@class="nav-link"]/p[contains(text(),"Структура")]')
    USERS = s('//a[@class="nav-link"]/p[contains(text(),"Пользователи")]')
    GROUPS = s('//a[@class="nav-link"]/p[contains(text(),"Группы")]')
    DOMAINS = s('//a[@class="nav-link"]/p[contains(text(),"Домены")]')
    DYNAMIC_GROUPS = s('//a[@class="nav-link"]/p[contains(text(),"Динамические группы")]')
    DEPARTMENTS = s('//a[@class="nav-link"]/p[contains(text(),"Подразделения")]')
    INVITATIONS = s('//a[@class="nav-link"]/p[contains(text(),"Приглашения")]')
    NOTIFICATIONS = s('//a[@class="nav-link"]/p[contains(text(),"Уведомления")]')
    # AUDIT
    EXECUTION_LOGS = s('//a[@class="nav-link"]/p[contains(text(),"Логи исполнения")]')
    OBJECTS = s('//a[@class="nav-link"]/p[contains(text(),"Объекты")]')
    SYSTEM_LOGINS = s('//a[@class="nav-link"]/p[contains(text(),"Входы в систему")]')
    HTTP_REQUESTS = s('//a[@class="nav-link"]/p[contains(text(),"HTTP запросы")]')
    ALL_LOGS = s('//a[@class="nav-link"]/p[contains(text(),"Все логи")]')
    # INVENTORY
    RESOURCE_AVAILABILITY = s('//a[@class="nav-link"]/p[contains(text(),"Наличие ресурсов")]')
    RESOURCE_CATALOG = s('//a[@class="nav-link"]/p[contains(text(),"Каталог ресурсов")]')
    # REPORTS
    TEMPLATES = s('//a[@class="nav-link"]/p[contains(text(),"Шаблоны")]')
    PREPARED_REPORTS = s('//a[@class="nav-link"]/p[contains(text(),"Готовые отчеты")]')
    TRENDS = s('//a[@class="nav-link"]/p[contains(text(),"Тренды")]')
    GRAPH = s('//a[@class="nav-link"]/p[contains(text(),"Граф")]')
    MAP = s('//a[@class="nav-link"]/p[contains(text(),"Карта")]')
    # STORAGE
    REPOSITORIES = s('//a[@class="nav-link"]/p[contains(text(),"Репозитории")]')
    FILES = s('//a[@class="nav-link"]/p[contains(text(),"Файлы")]')
    # ADMINISTRATION
    SETTINGS = s('//a[@class="nav-link"]/p[contains(text(),"Настройки")]')
    KEY_CLOAK = s('//a[@class="nav-link"]/p[contains(text(),"KeyCloak")]')
    SUB_NETWORKS = s('//a[@class="nav-link"]/p[contains(text(),"Подсети")]')
    BRIDGES = s('//a[@class="nav-link"]/p[contains(text(),"Мосты")]')
    BLACK_LIST = s('//a[@class="nav-link"]/p[contains(text(),"Черный список")]')
    WHITE_LIST = s('//a[@class="nav-link"]/p[contains(text(),"Белый список")]')
    CERTIFICATES = s('//a[@class="nav-link"]/p[contains(text(),"Сертификаты")]')
    SSH_ACCESS = s('//a[@class="nav-link"]/p[contains(text(),"SSH доступы")]')
    KICKSTART = s('//a[@class="nav-link"]/p[contains(text(),"Kickstart")]')
    LICENSE = s('//a[@class="nav-link"]/p[contains(text(),"Лицензия")]')


    @allure.step("Проверить наличие пунктов меню")
    def check_left_menu(self):
        l1_menu = [self.CONTROL_PANEL, self.REMOTE_ACCESS, self.MANAGEMENT_UEM, self.ORGANIZATION, self.AUDIT, self.INVENTORY, self.REPORTS, self.STORAGE, self.ADMINISTRATION]
        for menu_item in l1_menu:
            self.wait_element(menu_item)

        self.click(self.REMOTE_ACCESS, 'пункт меню [Удаленный доступ]')
        l2_remote_access = [self.DEVICES, self.SESSIONS, self.ADDRESSES, self.TAGS]
        for menu_item in l2_remote_access:
            self.wait_element(menu_item)

        self.click(self.MANAGEMENT_UEM, 'пункт меню [Управление (UEM)]')
        l2_management_uem = [self.POLICIES, self.TASKS, self.OS_INSTALLATION, self.REQUESTS]
        for menu_item in l2_management_uem:
            self.wait_element(menu_item)

        self.click(self.ORGANIZATION, 'пункт меню [Организация]')
        l2_organization = [self.STRUCTURE, self.USERS, self.GROUPS, self.DOMAINS, self.DYNAMIC_GROUPS, self.DEPARTMENTS, self.INVITATIONS, self.NOTIFICATIONS]
        for menu_item in l2_organization:
            self.wait_element(menu_item)

        self.click(self.AUDIT, 'пункт меню [Аудит]')
        l2_audit = [self.EXECUTION_LOGS, self.OBJECTS, self.SYSTEM_LOGINS, self.HTTP_REQUESTS, self.ALL_LOGS]
        for menu_item in l2_audit:
            self.wait_element(menu_item)

        self.click(self.INVENTORY, 'пункт меню [Инвентаризация]')
        l2_inventory = [self.RESOURCE_AVAILABILITY, self.RESOURCE_CATALOG]
        for menu_item in l2_inventory:
            self.wait_element(menu_item)

        self.click(self.REPORTS, 'пункт меню [Отчеты]')
        l2_reports = [self.TEMPLATES, self.PREPARED_REPORTS, self.TRENDS, self.GRAPH, self.MAP]
        for menu_item in l2_reports:
            self.wait_element(menu_item)

        self.click(self.STORAGE, 'пункт меню [Хранилище]')
        l2_storage = [self.REPOSITORIES, self.FILES]
        for menu_item in l2_storage:
            self.wait_element(menu_item)

        self.click(self.ADMINISTRATION, 'пункт меню [Администрирование]')
        l2_administration = [self.SETTINGS, self.KEY_CLOAK, self.SUB_NETWORKS, self.BRIDGES, self.BLACK_LIST, self.WHITE_LIST, self.CERTIFICATES, self.SSH_ACCESS, self.KICKSTART, self.LICENSE]
        for menu_item in l2_administration:
            self.wait_element(menu_item)


