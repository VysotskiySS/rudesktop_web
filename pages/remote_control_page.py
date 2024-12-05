import allure

from pages.base_page import BasePage
from selene.api import be, have, s
from config import *

class RemoteControlPage(BasePage):



    FIND_BTN = s('//button[contains(text(),"Найти")]')
    FILTER_SEARCH_FIELD = s('//input[@placeholder="Введите значение"]')
    CHECK_BOX_DEVICE_IN_LIST = s('//input[@class="action-select"]')
    ACTION_COUNTER = s('//span[@class="action-counter"]')
    '//td[@class="action-checkbox"]'

    IMPORT_DEVICES_FROM_FILE_BTN = s('//i[@class="fas fa-file-import"]')
    SELECT_ACTIONS = s('//select[@class="form-control"]')
    '//options[@value="delete_selected"]'
    '//options[@value="set_groups"]'
    '//options[@value="copy_to_address_book"]'
    '//options[@value="change_connection"]'
    '//options[@value="export"]'


    def filter_search(self):
        count_device_in_list = self.search_same_elements(self.CHECK_BOX_DEVICE_IN_LIST)
        self.set_text(self.FILTER_SEARCH_FIELD, '000111333')
        self.click(self.FIND_BTN, 'кнопка [Найти]')
        self.search_same_elements(self.CHECK_BOX_DEVICE_IN_LIST)
        self.get_attribute(self.ACTION_COUNTER, "data-actions-icnt")
        count_device_in_list_after_search = self.get_attribute(self.ACTION_COUNTER, "data-actions-icnt")