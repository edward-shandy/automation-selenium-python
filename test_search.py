from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import unittest
import time
import pytest



@pytest.fixture
def instagram_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    time.sleep(5)
    driver.quit()

@pytest.mark.regression
def test_search (instagram_driver):
    driver = instagram_driver
    driver.get('https://instagram.com/')
    username = "automation.edward"
    password = "User1234"
    wait = WebDriverWait(driver,10)

    try:
        username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        username_field.send_keys(username)

        password_field = wait.until(EC.presence_of_element_located((By.NAME,'password')))
        password_field.send_keys(password)

        button_login = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        button_login.click()

        wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="_aagx"]')))
        driver.refresh()
    except Exception as e:
            print (f"Error during login", str(e))
            return
    try:
        turnonbtn = driver.find_element(By.XPATH, '//button[text()="Turn On"]')
        turnonbtn.click()
    except:
        pass
    
    search_button = driver.find_element(By.XPATH, '//span[text()="Search"]')
    search_button.click()

    searchbox = driver.find_element(By.XPATH, '//input[@aria-label="Search input"]')
    searchbox.send_keys("Cristiano Ronaldo") 

if __name__ == "__main__":
    unittest.main()


