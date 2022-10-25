import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/ru/"


@pytest.fixture(scope='class')
def browser():
    print('\nstart browser...')
    browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    yield browser
    print('\nquit browser...')
    browser.quit()


class TestMainPage():
    @pytest.mark.open_page
    def test_1(self, browser):
        browser.get(link)

    @pytest.mark.view_products
    def test_2(self,browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//ul[@id='browse']//ul//a").click()

