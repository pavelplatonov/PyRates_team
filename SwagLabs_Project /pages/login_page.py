from .base_page import BasePage
from .locators import LoginLocators
from selenium.webdriver.common.by import By

link = 'https://www.saucedemo.com/'

class LoginPage(BasePage):

    def open_login_page(self):
        self.open_page()
        self.should_be_current_page(link)
