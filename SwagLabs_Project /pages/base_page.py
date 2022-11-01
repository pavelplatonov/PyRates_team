from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class BasePage():

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_page(self):
        self.browser.get(self.link)

    def click_element(self, method, locator):
        self.browser.find_element(method, locator).click()

    def sendkeys_element(self, method, locator, text):
        self.browser.find_element(method, locator).send_keys(text)

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def should_be_current_page(self, link):
        assert link in self.browser.current_url, 'wrong url'