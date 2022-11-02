from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class BasePage():

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link


    """Открывает ссылку"""

    def open_page(self):
        self.browser.get(self.link)


    """Нажатие на выбранный элемент из локаторов"""


    def click_element(self, method, locator):
        self.browser.find_element(method, locator).click()


    """Передает текст или нажание кнопок на клавиатуре"""


    def sendkeys_element(self, method, locator, text):
        self.browser.find_element(method, locator).send_keys(text)


    """Подтверждение наличия элемента на странице"""


    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True


    """Подтверждение текущего адреса страницы"""


    def should_be_current_page(self, link):
        assert link in self.browser.current_url, 'wrong url'