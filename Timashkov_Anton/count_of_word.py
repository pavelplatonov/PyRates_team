from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common import by as By

def count_of_word():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    try:
        driver.get("https://www.selenium.dev/")
        body = driver.find_element(By.By.TAG_NAME, 'body')
        body_text = body.text
        print("Count of words 'Selenium': ", end='')
        print(
            body_text.count('Selenium') + body_text.count('selenium') - body_text.count('selenium_') -
            body_text.count('}Selenium')
        )
    finally:
        driver.quit()


count_of_word()