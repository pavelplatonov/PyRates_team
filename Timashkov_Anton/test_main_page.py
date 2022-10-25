import pytest
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/ru/"

# class TestMainPage():
#     @pytest.mark.open_page
#     @pytest.mark.smoke

def test_go_to_catalogue(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_gatalog()

# def test_2(browser):
#     browser.get(link)
#     browser.find_element(By.XPATH, "//ul[@id='browse']//ul//a").click()
