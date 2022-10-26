import time
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def test_count_word_selenium():
    try:

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get("http://selenium.dev")

        count = driver.find_elements(By.XPATH, "//*[contains(text(), 'selenuim')]")
        count1 = driver.find_elements(By.XPATH, "//*[contains(text(), 'Selenium')]")
        count2 = len(count) + len(count1)

        assert count2 != 0, "вхождений искомого слова не найдено"
        print("успешно, число повторений: ", count2)
        print(" ")
        print("посчитал")

    finally:
        driver.quit()
