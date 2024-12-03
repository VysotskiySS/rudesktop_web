# file /rudesktop_web/pages/main_page.py
import allure

from pages.base_page import BasePage
from selene.api import be, have, s
from config import *

class MainPage(BasePage):
    # LEFT_MENU_L1
    CONTROL_PANEL = s('//a[@class="nav-link"]/p[contains(text(),"Панель управления")]')
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

    RESOURCE_AVAILABILITY = s('//a[@class="nav-link"]/p[contains(text(),"Наличие ресурсов")]')
    TEMPLATES = s('//a[@class="nav-link"]/p[contains(text(),"Шаблоны")]')
    PREPARED_REPORTS = s('//a[@class="nav-link"]/p[contains(text(),"Готовые отчеты")]')
    TRENDS = s('//a[@class="nav-link"]/p[contains(text(),"Тренды")]')
    GRAPH = s('//a[@class="nav-link"]/p[contains(text(),"Граф")]')
    MAP = s('//a[@class="nav-link"]/p[contains(text(),"Карта")]')


    @allure.step("Проверить наличие пунктов меню первого уровня")
    def check_left_menu(self):
        l1_menu = [self.REMOTE_ACCESS, self.MANAGEMENT_UEM, self.ORGANIZATION, self.AUDIT, self.INVENTORY, self.REPORTS, self.REPORTS, self.STORAGE, self.ADMINISTRATION]
        for menu_item in l1_menu:
            self.wait_element(menu_item)
            self.click(menu_item)