import time
import pytest
from pages.locators import LoginLocators
from pages.login_page import LoginPage
from selenium.webdriver.common.keys import Keys

link = 'https://www.saucedemo.com/'
valid_user = 'standard_user'
locked_out_user = 'locked_out_user'
problem_user = 'problem_user'
performance_glitch_user = 'performance_glitch_user'
password = 'secret_sauce'


"""TC_001.00.01 | Страница авторизации > Авторизация стандартного пользователя с валидными данными"""
@pytest.mark.smoke
def test_login_valid_user(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.keyboard_input(*LoginLocators.login_field, valid_user)
    page.keyboard_input(*LoginLocators.password_field, password)
    page.click_element(*LoginLocators.login_btn)
    page.should_be_current_page('https://www.saucedemo.com/inventory.html')


"""TC_001.00.02 | Страница авторизации > Авторизация заблокированного пользователя с валидными данными"""
def test_locked_out_user(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.keyboard_input(*LoginLocators.login_field, locked_out_user)
    page.keyboard_input(*LoginLocators.password_field, password)
    page.click_element(*LoginLocators.login_btn)
    error_text = page.find_element_text(*LoginLocators.error_warning)
    assert error_text == 'Epic sadface: Sorry, this user has been locked out.', 'wrong warning text'
    """скриншот результата"""
    page.take_screenshot(test_name='test_locked_out_user')


"""TC_001.00.03 | Страница авторизации > Авторизация проблемного пользователя с валидными данными"""
def test_problem_user(browser):
    page = LoginPage(browser, link)
    start = time.perf_counter()
    page.open_login_page()
    page.keyboard_input(*LoginLocators.login_field, problem_user)
    page.keyboard_input(*LoginLocators.password_field, password)
    page.click_element(*LoginLocators.login_btn)
    loading_time = time.perf_counter() - start
    page.should_be_current_page('https://www.saucedemo.com/inventory.html')
    # assert loading_time <= 15, 'loading time exceed 15 seconds'


"""TC_001.00.04 | Страница авторизации > Авторизация performance glitch user с валидными данными"""
@pytest.mark.xfail
def test_performance_glitch_user(browser):
    page = LoginPage(browser, link)
    start = time.perf_counter()
    page.open_login_page()
    page.keyboard_input(*LoginLocators.login_field, performance_glitch_user)
    page.keyboard_input(*LoginLocators.password_field, password)
    page.click_element(*LoginLocators.login_btn)
    loading_time = time.perf_counter()-start
    page.should_be_current_page('https://www.saucedemo.com/inventory.html')
    assert loading_time <= 15, 'loading time exceed 15 seconds'

"""TC_001.00.05 | Страница авторизации > Авторизация стандартного пользователя с валидным логином и пустым паролем"""
def test_login_valid_user_empty_password(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.keyboard_input(*LoginLocators.login_field, valid_user)
    page.click_element(*LoginLocators.login_btn)
    error_text = page.find_element_text(*LoginLocators.error_warning)
    assert error_text == 'Epic sadface: Password is required', "wrong warning text"
    page.take_screenshot(test_name='test_empty_password')


"""TC_001.00.06 | Страница авторизации > Авторизация с невалидным пользователем и валидным паролем"""
def test_login_invalid_user_valid_password(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.keyboard_input(*LoginLocators.login_field, 'admin')
    page.keyboard_input(*LoginLocators.password_field, password)
    page.click_element(*LoginLocators.login_btn)
    error_text = page.find_element_text(*LoginLocators.error_warning)
    assert error_text == 'Epic sadface: Username and password do not match any user in this service', 'wrong warning text'
    page.take_screenshot(test_name='test_login_invalid_user')


"""TC_001.00.07 | Страница авторизации > Авторизация стандартного пользователя с невалидным паролем"""
def test_login_valid_user_invalid_password(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.keyboard_input(*LoginLocators.login_field, valid_user)
    page.keyboard_input(*LoginLocators.password_field, '%password')
    page.click_element(*LoginLocators.login_btn)
    error_text = page.find_element_text(*LoginLocators.error_warning)
    assert error_text == 'Epic sadface: Username and password do not match any user in this service', 'wrong warning text'
    page.take_screenshot(test_name='test_invalid_password')


"""TC_001.00.09 | Страница авторизации > Авторизация стандартного пользователя с валидными данными и вводом через Enter"""
def test_login_valid_user_valid_password_enter_btn(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.keyboard_input(*LoginLocators.login_field, valid_user)
    page.keyboard_input(*LoginLocators.password_field, password)
    page.keyboard_input(*LoginLocators.password_field, Keys.RETURN)
    page.should_be_current_page('https://www.saucedemo.com/inventory.html')
