from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_simple():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    try:
        driver.get("https://www.selenium.dev/")

        assert driver.title == 'Selenium'
    finally:
        driver.quit()
