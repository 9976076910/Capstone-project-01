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
class TestEmpdelete:
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
    

            # This will scroll the Webpage
            self.driver.execute_script('window.scrollBy(0, 800)')
            # Used to Locate and send the Username
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.NAME, locator.WebLocators().usernameLocator))).send_keys(
                data.WebDatas().username)
            # Used to locate and send the Password
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.NAME, locator.WebLocators().passLocator))).send_keys(
                data.WebDatas().password)
            # Login
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocators().subLocator))).click()
            self.driver.execute_script('window.scrollBy(0, 800)')
            # Clicking PIM
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocators().pimLocator))).click()
            # deleting an existing user
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocators().deleteLocator))).click()
            # Confirming the alert Msg
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocators().alertLocator))).click()
