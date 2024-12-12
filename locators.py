from selene.api import s

class SystemLocators:
    details_btn = s('//button[contains(.,"Дополнительные")]')
    go_unsafe = s("//a[contains(text(), 'Перейти на сайт')]")

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
    TASK_QUEUE = s('//a[@class="nav-link"]/p[contains(text(),"Очередь задач")]')
    BLACK_LIST = s('//a[@class="nav-link"]/p[contains(text(),"Черный список")]')
    WHITE_LIST = s('//a[@class="nav-link"]/p[contains(text(),"Белый список")]')
    CERTIFICATES = s('//a[@class="nav-link"]/p[contains(text(),"Cертификаты")]') # Бага в слове, исправил для прохода в процессе написания, исправить
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
    SUCCESS_ALERT = s('//div[@class="alert alert-success alert-dismissible"]')

    MORE_OPTION_BTN = s('//div[@class="dropdown table-action"]')
    OPTION_DELETE = s('//a[contains(@href, "/delete/")]')

    MAIN_CHECK_BOX = s('//input[@id="action-toggle"]')
    SELECTOR = s('//select[@name="action"]')
    DELETE_SELECTED = s('//option[@value="delete_selected"]')
    EXECUTE_BTN = s('//button[contains(text(), "Выполнить")]')
    SUBMIT_BTN = s('//input[@type="submit"]')
    ACTION_COUNTER = s('//span[@class="action-counter"]')

    COUNT_ELEMENTS = s('//table[@class="table table-striped"]')

class LoginLocators:
    ENTER_AGAIN_BTN = s('//a[@href="/"]')
    LOGIN_MSG = s('//p[@class="login-box-msg"]')
    PASSWORD_FIELD = s('//input[@id="password"]')

    LOGIN_FIELD = s('//input[@name="username"]')
    # EMAIL_FIELD = s('input[placeholder="Адрес электронной почты"]')
    EMAIL_FIELD = s('//input[@name="email"]')
    FULL_NAME_FIELD = s('//input[@name="full_name"]')
    PHONE_FIELD = s('//input[@name="phone"]')
    REG_PASSWORD_FIELD = s('//input[@name="password1"]')
    REG_PASSWORD_CONFIRM = s('//input[@name="password2"]')
    REGISTRATION_BTN = s('//button[contains(text(), "Зарегистрироваться") and @type="submit"]')

    METHOD_AUTH = s('//select[@name="domain"]')
    DOMAIN_SELECTOR = s('//option[@value="@win2012.local"]')
    LOCAL_SELECTOR = s('//option[@value="@Локальный"]')
    SUBMIT_BTN = s('//button[@type="submit"]')
    RESTORE_PASS = s('//a[contains(text(),"Забыли свой пароль или имя пользователя?")]')
    LOGIN_ICON = s('li.nav-item.dropdown')
    LOGO = s('img[alt="RuDesktop"]')

    MSG_RECOVERY = s('//div[@class="card-body"]')
    LOGOUT_BTN = s('//a[@href="/logout/"]')
    LOGIN_AGAIN_BTN = s('//a[@class="btn btn-primary btn-block"]')
    CREATE_USER = s('//a[@href="/account/register/"]')

    I_HAVE_PROFILE = s('//a[@href="/login/"]')
    ENTER_BTN = s('//button[contains(text(), "Войти")]')

class RemoteAccessLocators:
    ADD_ADDRESS = s('//a[@href="/addressbook/address/add/"]')
    SAVE_BTN = s('//input[@value="Сохранить"]')
    SAVE_AND_CONTINUE_BTN = s('//input[@value="Сохранить и продолжить"]')
    ID_FIELD = s('//input[@name="peer"]')
    NAME_FIELD = s('//input[@name="alias"]')
    ADD_TAG = s('//a[@href="/addressbook/tag/add/"]')
    NAME_TAG_FIELD = s('//input[@name="name"]')

    FIND_BTN = s('//button[contains(text(),"Найти")]')
    FILTER_SEARCH_FIELD = s('//input[@placeholder="Введите значение"]')
    CHECK_BOX_DEVICE_IN_LIST = s('//input[@class="action-select"]')

    IMPORT_DEVICES_FROM_FILE_BTN = s('//i[@class="fas fa-file-import"]')
    SELECT_ACTIONS = s('//select[@class="form-control"]')
    # '//options[@value="delete_selected"]'
    # '//options[@value="set_groups"]'
    # '//options[@value="copy_to_address_book"]'
    # '//options[@value="change_connection"]'
    # '//options[@value="export"]'
    # '//td[@class="action-checkbox"]'


class UEMLocators:
    ADD_POLICY_BTN = s('//a[@href="/automation/policy/add/"]')
    SEARCH_FIELD = s('//input[@placeholder="Поиск..."]')
    TEMPLATE_FOR_NEW_POLICY = s('//a[@href="/automation/policy/create/?template=default"]')
    # Категории политик
    USERS_POLICY = s('//div[contains(text(), "Пользовательские")]')
    MAINTENANCE_AND_ADMINISTRATION_POLICY = s('//div[contains(text(), "Обслуживание и администрирование")]')
    INVENTORY = s('//a[@href="/automation/policy/create/?template=setup"]')

    SERVER_MAINTENANCE_POLICY = s('//div[contains(text(), "Обслуживание сервера RuDesktop")]')
    SECURITY_AND_ACCESS_MANAGEMENT_POLICY = s('//div[contains(text(), "Управление безопасностью и доступом")]')
    DIRECTORY_AND_FILE_MANAGEMENT_POLICY = s('//div[contains(text(), "Управление директориями и файлами")]')
    USER_AND_DEVICE_MANAGEMENT_POLICY = s('//div[contains(text(), "Управление пользователями и устройствами")]')
    SOFTWARE_INSTALLATION_AND_UPDATE_POLICY = s('//div[contains(text(), "Установка и обновление ПО")]')
    POLICY_GROUPS_LIST = [MAINTENANCE_AND_ADMINISTRATION_POLICY, SERVER_MAINTENANCE_POLICY, SECURITY_AND_ACCESS_MANAGEMENT_POLICY, DIRECTORY_AND_FILE_MANAGEMENT_POLICY, USER_AND_DEVICE_MANAGEMENT_POLICY, SOFTWARE_INSTALLATION_AND_UPDATE_POLICY]

    NAME_FIELD = s('//input[@name="name"]')
    SAVE_BTN = s('//button[contains(text(), "Сохранить") and contains(@class, "btn-primary")]')
    ADD_TASK_BTN = s('//a[@href="/automation/job/add/"]')


class OrgLocators:
    ENABLE_CHECKBOX = s('//input[@name="enable"]')
    TYPE_AD_SELECTOR = s('//span[@title="Active Directory"]')
    ADD_DOMAIN_BTN = s('//a[@href="/ad/domain/add/"]')
    DOMAIN_FIELD = s('//input[@name="domain"]')
    ADDRESS_DC_FIELD = s('//input[@name="host"]')
    USE_TLS_CHECKBOX = s('//input[@name="use_tls"]')
    USER_FIELD = s('//textarea[@name="user"]')
    PASSWORD_FIELD = s('//input[@name="password"]')
    PATH_FIELD = s('//textarea[@name="path"]')
    SAVE_BTN = s('//input[@value="Сохранить"]')