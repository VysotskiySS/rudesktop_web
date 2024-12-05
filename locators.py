from selene.api import be, have, s
from config import *

class MenuLocators:
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

class HeaderLocators:
    PUSH_MENU_BTN = s('//*[@data-widget="pushmenu"]')
    SEARCH_FIELD = s('//input[@type="search"]')
    LOGIN_ICON = s('li.nav-item.dropdown')
    PROFILE = s('//a[@href="/account/user/2/change/"]')
    CHANGE_PASSWORD = s('//a[@href="/password_change/"]')
    LOGOUT = s('//a[@href="/logout/"]')
    ACTIVE_BREAD_CRUMB = s('//li[@class="breadcrumb-item active"]')

class MainLocators:
    OLD_PASSWORD_FIELD = s('//input[@name="old_password"]')
    NEW_PASSWORD_FIELD = s('//input[@name="new_password1"]')
    CONFIRM_NEW_PASSWORD_FIELD = s('//input[@name="new_password2"]')
    CHANGE_PASSWORD_BTN = s('//*[@value="Изменить пароль"]')

    SUCCESS_MSG = s('//div[@class="callout callout-success"]')
    DANGER_MSG = s('//div[@class="callout callout-danger"]')
    ERROR_LIST = s('//ul[@class="errorlist"]')

class LoginLocators:
    ENTER_AGAIN_BTN = s('//a[@href="/"]')
    LOGIN_MSG = s('//p[@class="login-box-msg"]')
    PASSWORD_FIELD = s('//input[@id="password"]')
    LOGIN_FIELD = s('//input[@id="username"]')
    METHOD_AUTH = s('//select[@name="domain"]')
    DOMAIN_SELECTOR = s('//option[value="@win2012.local"]')
    LOCAL_SELECTOR = s('//option[value="@Локальный"]')
    SUBMIT_BTN = s('//button[@type="submit"]')
    RESTORE_PASS = s('//a[contains(text(),"Забыли свой пароль или имя пользователя?")]')
    LOGIN_ICON = s('li.nav-item.dropdown')
    LOGO = s('img[alt="RuDesktop"]')
    EMAIL_FIELD = s('input[placeholder="Адрес электронной почты"]')
    MSG_RECOVERY = s('//div[@class="card-body"]')
    LOGOUT_BTN = s('//a[@href="/logout/"]')
    LOGIN_AGAIN_BTN = s('//a[@class="btn btn-primary btn-block"]')