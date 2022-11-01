from .base_page import BasePage
from .locators import LoginLocators
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

link = 'https://www.saucedemo.com/'

class LoginPage(BasePage):

    def open_login_page(self):
        self.open_page()
        self.should_be_current_page(link)

    def find_element_text(self, method, locator):
        elem = self.browser.find_element(method, locator)
        text = elem.text
        return text