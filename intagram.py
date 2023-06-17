from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
import time
import pytest
import pytest_selenium


s = Service('D:\\Documents\\Learning\\automation-selenium-python\\chrome-driver\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://sandbox.octav.prieds.com/')


