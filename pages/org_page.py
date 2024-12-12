# file /rudesktop_web/pages/org_page.py
import allure
from locators import *
from pages.base_page import BasePage
from config import *


class OrgPage(BasePage):

    @allure.step("Открыть страницу [Домены]")
    def open_domains(self):
        self.click(MenuLocators.ORGANIZATION, 'пункт меню [Организация]')
        self.click(MenuLocators.DOMAINS, 'пункт меню [Домены]')

    @allure.step("Добавить домен")
    def add_domain(self, domain='win2012.local', password='Kief22Mo'):
        self.click(OrgLocators.ADD_DOMAIN_BTN, 'кнопка [Добавить Домен]')
        self.set_text(OrgLocators.DOMAIN_FIELD, domain)
        self.set_text(OrgLocators.ADDRESS_DC_FIELD, '192.168.10.68')
        self.set_text(OrgLocators.USER_FIELD, 'CN=Администратор,CN=Users,DC=win2012,DC=local')
        self.set_text(OrgLocators.PASSWORD_FIELD, password)
        self.click(OrgLocators.SAVE_BTN, 'кнопка [Сохранить]')
        self.wait_element(MainLocators.SUCCESS_ALERT)