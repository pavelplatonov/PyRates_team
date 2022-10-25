from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def go_to_catalog(self):
        self.browser.find_element(By.XPATH, "//ul[@id='browse']//ul//a").click()
