from pages.locators import LoginLocators
from pages.login_page import LoginPage
from time import sleep

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
    page.should_be_current_page('https://www.saucedemo.com/inventory.html')

def test_locked_out_user(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.sendkeys_element(*LoginLocators.login_field, locked_out_user)
    page.sendkeys_element(*LoginLocators.password_field, password)
    page.click_element(*LoginLocators.login_btn)

def test_problem_user(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.sendkeys_element(*LoginLocators.login_field, problem_user)
    page.sendkeys_element(*LoginLocators.password_field, password)
    page.click_element(*LoginLocators.login_btn)
    page.should_be_current_page('https://www.saucedemo.com/inventory.html')

def test_performance_glitch_user(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.sendkeys_element(*LoginLocators.login_field, performance_glitch_user)
    page.sendkeys_element(*LoginLocators.password_field, password)
    page.click_element(*LoginLocators.login_btn)
    page.should_be_current_page('https://www.saucedemo.com/inventory.html')

def test_login_valid_user_empty_password(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.sendkeys_element(*LoginLocators.login_field, valid_user)
    page.click_element(*LoginLocators.login_btn)
    error_text = page.find_element_text(*LoginLocators.error_warning)
    assert error_text == 'Epic sadface: Password is required', "wrong warning text"
    sleep(5)