from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_simple():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("http://selenium.dev")

    assert driver.title == 'Selenium'

    driver.quit()
