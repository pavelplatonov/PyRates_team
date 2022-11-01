from pages.locators import LoginLocators
from pages.login_page import LoginPage

link = 'https://www.saucedemo.com/'
valid_user = 'standard_user'
locked_out_user = 'locked_out_user'
problem_user = 'problem_user'
performance_glitch_user = 'performance_glitch_user'
password = 'secret_sauce'


def test_open_login_page(browser):
    page = LoginPage(browser, link)
    page.open_login_page()

def test_login_valid_user(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.sendkeys_element(*LoginLocators.login_field, valid_user)
    page.sendkeys_element(*LoginLocators.password_field, password)
    page.click_element(*LoginLocators.login_btn)
