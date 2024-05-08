from Data import data
from Locator import locators
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pytest


# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class TestEmpAdd:
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
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.NAME, locators.WebLocators().usernameLocator))).send_keys(
            data.WebDatas().username)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.NAME, locators.WebLocators().passLocator))).send_keys(
            data.WebDatas().password)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locators.WebLocators().subLocator))).click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locators.WebLocators().pimLocator))).click()

        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locators.WebLocators().addLocator))).click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.NAME, locators.WebLocators().firstnameLocator))).send_keys(
            data.WebDatas().firstname)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.NAME, locators.WebLocators().LastnameLocator))).send_keys(
            data.WebDatas().lastName)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locators.WebLocators().saveLocator))).click()
        self.driver.execute_script('window.scrollBy(0, 800)')
        add = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locators.WebLocators().conLocator)))
        self.driver.execute_script("arguments[0].click();", add)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locators.WebLocators().buttonLocator))).click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locators.WebLocators().submitLocator))).click()
        self.driver.execute_script('window.scrollBy(0, 800)')