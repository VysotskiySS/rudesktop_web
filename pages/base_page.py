# file /rudesktop_web/pages/base_page.py

import ast
import random
import string
import re
import time
from itertools import count

from faker import Faker
import allure
import pytest
from selene import query, be
from selene.support.shared import browser
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import *


class BasePage:


    @allure.step("Переход на страницу '{url}'")
    def open_url(self, url):
        browser.open(url)

    def element(self, locator):
        return browser.element(locator)

    def elements(self, locator):
        return browser.all(locator)

    def get_element_text(self, element, element_name=None):
        if element_name is not None:
            with allure.step(f"Получение текста из элемента '{element_name}'"):
                return element.get(query.text)
        else:
            return element.get(query.text)

    def open_unsafe(self):
        try:
            SystemLocators.details_btn.click()
            SystemLocators.go_unsafe.click()
        except:
            pass

    @allure.step("Проверка значения атрибута placeholder элемента")
    def assert_placeholder(self, element, text):
        element = element()
        placeholder_value = element.get_attribute("placeholder")
        assert placeholder_value == text, f"Unexpected placeholder value: {placeholder_value}"

    @allure.step("Взять тело из элемента '{element_name}'")
    def get_element_value(self, element, element_name):
        return element.get(query.tag)

    def set_text(self, element, text, element_name=None):
        if text is not None:
            with allure.step(f"Заполнение поля '{element_name}' текстом '{text}'"):
                element.set_value(text)
        else:
            element.set_value(text)

    def click(self, element, text=None):
        if text is not None:
            with allure.step(f"Клик по элементу '{text}'"):
                element.click()
                self.wait_a_moment()
                self.get_screenshot()
        else:
            element.click()
            self.wait_a_moment()
            self.get_screenshot()

    def wait_text(self, text, timeout=10):
        """
        Ожидает появления указанного текста на странице.

        :param text: Текст, который нужно ожидать.
        :param timeout: Максимальное время ожидания в секундах.
        """
        # Ожидаем, что текст появится где-либо в теле страницы
        browser.with_(timeout=timeout).should(have.text(text))

    # @allure.step("Получение атрибута")
    def get_attribute(self, element, attribute):
        return element.get(query.attribute(attribute))

    def get_int_from_str(self, input_string):
        match = re.search(r'\d+', input_string)
        if match:
            number = int(match.group(0))
            print(number)
        return number

    # @allure.step("Получение текущего url")
    def get_url(self):
        return browser.driver.current_url

    # @allure.step("Перемещение к элементу")
    def move_to(self, element):
        driver = browser.driver
        action = ActionChains(driver)
        action.move_to_element(element).perform()

    def get_element(self, locator):
        driver = browser.driver
        return driver.find_element(By.XPATH, locator)

    def get_element_amount(self, locator):
        elements = browser.all(locator)
        return len(elements)

    @staticmethod
    def get_random_element_from_list(elements_list):
        return elements_list[random.randrange(0, len(elements_list))]

    def get_random_element(self, locator):
        # count = self.get_element_amount(locator)
        # counter = random.randrange(0, count - 1)
        # elements_list = self.elements(locator)
        # return elements_list[counter]

        elements_list = self.elements(locator)
        count = self.get_element_amount(locator)
        counter = random.randrange(0, count - 1)
        random_element = elements_list[counter]
        return random_element

        # self.click(list[counter])

    def click_random_element(self, locator):
        list = self.elements(locator)
        count = self.get_element_amount(locator)
        counter = random.randrange(0, count - 1)
        self.click(list[counter])

    def get_elements(self, locator):
        driver = browser.driver
        return driver.find_elements(By.XPATH, locator)

    def wait_a_second(self):
        time.sleep(1)

    def wait_a_moment(self):
        time.sleep(0.5)

    def wait_element(self, locator, text=None):
        if text is not None:
            with allure.step(f"Проверка наличия элемента '{text}'"):
                locator.should(be.visible)
        else:
            locator.should(be.visible)

    @allure.step("Проверка отсутствия элемента")
    def wait_element_not_visible(self, locator):
        locator.should(be.hidden)

    def wait_element_hidden(self, element, text=None):
        if text is not None:
            with allure.step(f"Проверка отсутствия элемента '{text}'"):
                element.should(be.hidden)
        else:
            element.should(be.hidden)

    @allure.step("Сравнение значений {expression1} и {expression2}")
    def assert_check_expressions(self, expression1, expression2, element_name=None):
        assert expression1 == expression2, print(element_name)
        self.get_screenshot()

    @allure.step("Проверка не соответсвия значений {expression1} и {expression2}")
    def assert_check_not_expressions(self, expression1, expression2, element_name=None):
        assert expression1 != expression2, print(element_name)

    @allure.step("Проверка наличия текста {expression1} в {expression2}")
    def assert_check_coincidence(self, expression1, expression2, element_name):
        assert expression1 in expression2, print(element_name)
        self.get_screenshot()

    @allure.step("Проверка числового значения в пределах {value_from} в {value_to}")
    def assert_check_range(self, value_from, value_to, value_check, element_name):
        assert value_from <= value_check <= value_to, print(element_name)

    @allure.step("Сравнение значений {expression1} больше {expression2}")
    def assert_check_comparison(self, expression1, expression2, element_name):
        assert expression1 > expression2, print(element_name)

    @allure.step("Клик Enter в поле '{fieldName}'")
    def push_enter(self, element, element_name):
        element.send_keys(Keys.ENTER)

    @allure.step("Клик Backspace в поле '{fieldName}'")
    def push_backspace(self, element, element_name):
        element.send_keys(Keys.BACKSPACE)

    # @allure.step("Очистить поле '{fieldName}'")
    def field_clear(self, element, element_name=None):
        if element_name is not None:
            with allure.step(f"Очистка поля '{element_name}'"):
                element.clear()
        else:
            element.clear()

        element.clear()

    @allure.step("Назад в браузере")
    def browser_back(self):
        browser.driver.back()
        self.wait_a_second()

    @allure.step("Поиск количества одинаковых элементов")
    def search_same_elements(self, element):
        '''
        Docstring: выполнение поиска количества одинаковых элементов на странице
        :param element: локатор
        :return: количество элементов, число
        '''
        elements = browser.all(element)
        count = 0
        for element in elements:
            count += 1
            print(elements)

        return count

    # @staticmethod
    def get_screenshot(self):
        allure.attach(
            name="Скриншот",
            body=browser.driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG,
        )
    # @staticmethod
    # def get_screenshot():
    #     screen = "screen.png"
    #     browser.driver.get_screenshot_as_png(screen)
    #     allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)
        # pass

    @staticmethod
    def get_title():
        return browser.driver.title

    @staticmethod
    def get_random_element(elements_list):
        return elements_list[random.randrange(0, len(elements_list))]

    # @allure.step("Получение числа из строки")
    def get_number_from_element(self, element):
        return int(re.sub('[^0-9]', "", self.get_element_text(element)))

    # @allure.step("get_field_value js")
    def execute_script(self, script):
        return browser.driver.execute_script(script)

    # @allure.step("Получение тега элемента")
    def get_element_tag(self, element):
        return element.get(query.tag)

    @allure.step("Проверка цвета элемента")
    def checking_color(self, element, color):
        rgba = element.get(query.css_property('color'))
        r, g, b, alpha = ast.literal_eval(rgba.strip("rgba"))
        hex_value = '#%02x%02x%02x' % (r, g, b)
        assert hex_value == color, print(f"Цвет элемента не соответствует '{color}'")

    @allure.step("Обновление страницы")
    def reload_page(self):
        browser.driver.refresh()

    # @allure.step("Распарсить многострочную строку")
    def parse_multiline_string(self, string):
        string = string.split('\n')
        return string

    @allure.step("Проверить активный элемент в хлебных крошках на соответствие тексту")
    def assert_active_bread_crumbs(self, reference_text):
        current_text = self.get_element_text(HeaderLocators.ACTIVE_BREAD_CRUMB)
        assert current_text == reference_text, f'Текст активной страницы в хлебных крошках должен быть {reference_text} но получен {current_text}'

    @allure.step("Генерируем случайное имя")
    def generate_random_name(self, base_name='username', length=5):
        # Генерируем случайную строку из букв заданной длины
        random_part = ''.join(random.choices(string.ascii_letters, k=length))
        # Возвращаем полное имя, состоящее из постоянной и случайной части
        return f"{base_name}_{random_part}"

    @allure.step("Генерируем случайный адрес почты")
    def generate_random_email(self, base_email='rude', length=8):
        # Генерируем случайную строку из букв заданной длины
        random_part = ''.join(random.choices(string.ascii_lowercase, k=length))
        # Возвращаем полный адрес, состоящее из постоянной и случайной части
        return f"{base_email}-{random_part}@mailforspam.com"

    @allure.step("Генерируем случайное ФИО")
    def generate_random_full_name(self):
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        return f"{first_name} {last_name} Rudesktopovich"