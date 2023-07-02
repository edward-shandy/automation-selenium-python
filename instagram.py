from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import unittest
import time


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.username = "automation.edward"
        self.password = "User1234"
        self.refresh = self.driver.refresh()

    def test_login_page (self):
        driver = self.driver
        driver.get('https://instagram.com/')
        wait = WebDriverWait(driver,10)

        username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        username_field.send_keys(self.username)

        password_field = wait.until(EC.presence_of_element_located((By.NAME,'password')))
        password_field.send_keys(self.password)

        button_login = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        button_login.click()

        wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="_aagx"]')))
        self.driver.refresh()
    

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

#notes
