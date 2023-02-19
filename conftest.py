import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import valid_email, valid_password

@pytest.fixture(scope="session", autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:\\driver\\chromedriver.exe')
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   yield
   pytest.driver.quit()

@pytest.fixture(scope="session")
def autorized():
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   pytest.driver.find_element(By.ID, "email").send_keys(valid_email)
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   pytest.driver.find_element(By.ID, "pass").send_keys(valid_password)
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

