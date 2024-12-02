# file /rudesktop_web/pages/main_page.py

from pages.base_page import BasePage
from selene.api import be, have, s
from config import *

class MainPage(BasePage):
    DASHBOARD_AND_CONTROL_PANEL = s('//a[@class="nav-link"] and //p[contains(text(),"Панель управления")]')
    REMOTE_ACCESS = s('//a[@class="nav-link"] and //p[contains(text(),"Удаленный доступ")]')
    MANAGEMENT_UEM = s('//a[@class="nav-link"] and //p[contains(text(),"Управление (UEM)")]')
    ORGANIZATION = s('//a[@class="nav-link"] and //p[contains(text(),"Организация")]')
    AUDIT = s('//a[@class="nav-link"] and //p[contains(text(),"Аудит")]')
    INVENTORY = s('//a[@class="nav-link"] and //p[contains(text(),"Инвентаризация")]')
    REPORTS = s('//a[@class="nav-link"] and //p[contains(text(),"Отчеты")]')
    STORAGE = s('//a[@class="nav-link"] and //p[contains(text(),"Хранилище")]')
    ADMINISTRATION = s('//a[@class="nav-link"] and //p[contains(text(),"Администрирование")]')

    DEVICES = s('//a[@class="nav-link"] and //p[contains(text(),"Устройства")]')
    SESSIONS = s('//a[@class="nav-link"] and //p[contains(text(),"Сессии")]')
    ADDRESSES = s('//a[@class="nav-link"] and //p[contains(text(),"Адреса")]')
    TAGS = s('//a[@class="nav-link"] and //p[contains(text(),"Теги")]')

    POLICIES = s('//a[@class="nav-link"] and //p[contains(text(),"Политики")]')
    TASKS = s('//a[@class="nav-link"] and //p[contains(text(),"Задачи")]')
    OS_INSTALLATION = s('//a[@class="nav-link"] and //p[contains(text(),"Установка OS")]')
    REQUESTS = s('//a[@class="nav-link"] and //p[contains(text(),"Обращения")]')

    STRUCTURE = s('//a[@class="nav-link"] and //p[contains(text(),"Структура")]')
    USERS = s('//a[@class="nav-link"] and //p[contains(text(),"Пользователи")]')
    GROUPS = s('//a[@class="nav-link"] and //p[contains(text(),"Группы")]')
    DOMAINS = s('//a[@class="nav-link"] and //p[contains(text(),"Домены")]')
    DYNAMIC_GROUPS = s('//a[@class="nav-link"] and //p[contains(text(),"Динамические группы")]')
    DEPARTMENTS = s('//a[@class="nav-link"] and //p[contains(text(),"Подразделения")]')
    INVITATIONS = s('//a[@class="nav-link"] and //p[contains(text(),"Приглашения")]')
    NOTIFICATIONS = s('//a[@class="nav-link"] and //p[contains(text(),"Уведомления")]')

    EXECUTION_LOGS = s('//a[@class="nav-link"] and //p[contains(text(),"Логи исполнения")]')
    OBJECTS = s('//a[@class="nav-link"] and //p[contains(text(),"Объекты")]')
    SYSTEM_LOGINS = s('//a[@class="nav-link"] and //p[contains(text(),"Входы в систему")]')
    HTTP_REQUESTS = s('//a[@class="nav-link"] and //p[contains(text(),"HTTP запросы")]')
    ALL_LOGS = s('//a[@class="nav-link"] and //p[contains(text(),"Все логи")]')

    RESOURCE_AVAILABILITY = s('//a[@class="nav-link"] and //p[contains(text(),"Наличие ресурсов")]')
    ADMINISTRATION = s('//a[@class="nav-link"] and //p[contains(text(),"Администрирование")]')

    TEMPLATES = s('//a[@class="nav-link"] and //p[contains(text(),"Шаблоны")]')
    PREPARED_REPORTS = s('//a[@class="nav-link"] and //p[contains(text(),"Готовые отчеты")]')
    TRENDS = s('//a[@class="nav-link"] and //p[contains(text(),"Тренды")]')
    GRAPH = s('//a[@class="nav-link"] and //p[contains(text(),"Граф")]')
    MAP = s('//a[@class="nav-link"] and //p[contains(text(),"Карта")]')
