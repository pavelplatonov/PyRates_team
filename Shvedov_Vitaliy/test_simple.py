from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from urllib.request import urlopen


def test_simple():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("http://selenium.dev")

    assert driver.title == 'Selenium'

    driver.quit()

    response = urlopen("http://selenium.dev")
    html = response.read().decode('utf-8')
    subs = 'Selenium'
    cnt = html.count(subs)
    print("Количество упоминаний 'Selenium':", cnt)
