import allure

from locators import MainLocators, MenuLocators, RemoteAccessLocators, HeaderLocators
from pages.base_page import BasePage
from selene.api import be, have, s
from config import *
import time
from bs4 import BeautifulSoup
from selenium import webdriver

class MapperPage(BasePage):
    # Настройки Selenium

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Если вы хотите, чтобы браузер запускался без GUI
    driver = webdriver.Chrome(options=options)

    # Данные для авторизации
    login_url = "https://192.168.10.74/login/?next=/"
    base_url = "https://192.168.10.74"
    username = "rude"
    password = "Kief22Mo"

    # Построение карты сайта из главной страницы
    def build_sitemap(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        links = set()

        # Собираем все ссылки на страницы
        for link in soup.find_all('a', href=True):
            url = link['href']
            if url.startswith('/'):
                url = self.base_url + url
            if url.startswith(self.base_url):
                links.add(url)
        return links

    # Проверка открытия каждой страницы
    def check_pages(self, links):
        for link in links:
            try:
                self.driver.get(link)
                time.sleep(2)
                print(f"Successfully opened {link}")
            except Exception as e:
                print(f"Failed to open {link}: {e}")