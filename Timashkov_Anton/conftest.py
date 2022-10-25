import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope='class')
def browser():
    print('\nstart browser...')
    browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    yield browser
    print('\nquit browser...')
    browser.quit()
