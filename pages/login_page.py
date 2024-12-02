from pages.base_page import BasePage
from selene.api import be, have, s

class LoginPage(BasePage):
    details_btn = s('//button[contains(.,"Дополнительные")]')
    go_unsafe = s("//a[contains(text(), 'Перейти на сайт')]")

    def login(self):
        self.click(self.details_btn)
        self.click(self.go_unsafe)


