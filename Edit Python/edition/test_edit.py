from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pytest


# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class TestEmpedit:
    @pytest.fixture
    def boot(self):
        # Setup before testing
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)
        yield
        # Teardown after testing
        self.driver.quit()

    def test_login(self,boot):

            self.driver.execute_script('window.scrollBy(0, 800)')
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.NAME, locator.WebLocators().usernameLocator))).send_keys(
                data.WebDatas().username)
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.NAME, locator.WebLocators().passLocator))).send_keys(
                data.WebDatas().password)
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocators().subLocator))).click()
            self.driver.execute_script('window.scrollBy(0, 800)')
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocators().pimLocator))).click()
            self.driver.execute_script('window.scrollBy(0, 800)')
            edit = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocators().editLocator)))
            self.driver.execute_script("arguments[0].click();", edit)
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocators().DOBLocator))).send_keys(
                data.WebDatas().DOB)

            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocators().buttonLocator))).click()
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocators().maritalLocator))).click()
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocators().marriedLocator))).click()

            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocators().conLocator))).click()
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocators().saveeLocator))).click()