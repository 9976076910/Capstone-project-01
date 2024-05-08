from Data import data
from Locators import locator


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep


# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




class Empedit:


   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.wait = WebDriverWait(self.driver, 10)


   def boot(self):
       self.driver.get(data.WebDatas().url)
       self.driver.maximize_window()




   def quit(self):
       self.driver.quit()


   def login(self):
       try:
           self.boot()
           self.driver.execute_script('window.scrollBy(0, 800)')
           self.wait.until(ec.presence_of_element_located((By.NAME, locator.WebLocators().usernameLocator))).send_keys(
               data.WebDatas().username)
           self.wait.until(ec.presence_of_element_located((By.NAME, locator.WebLocators().passLocator))).send_keys(
               data.WebDatas().password)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locator.WebLocators().subLocator))).click()
           self.driver.execute_script('window.scrollBy(0, 800)')
           self.wait.until(
               ec.presence_of_element_located((By.XPATH, locator.WebLocators().pimLocator))).click()
           self.driver.execute_script('window.scrollBy(0, 800)')
           edit = self.wait.until(ec.presence_of_element_located((By.XPATH, locator.WebLocators().editLocator)))
           self.driver.execute_script("arguments[0].click();", edit)
           self.wait.until(
               ec.presence_of_element_located((By.XPATH, locator.WebLocators().DOBLocator))).send_keys(
               data.WebDatas().DOB)

           self.wait.until(
               ec.presence_of_element_located((By.XPATH, locator.WebLocators().buttonLocator))).click()
           self.wait.until(
               ec.presence_of_element_located((By.XPATH, locator.WebLocators().maritalLocator))).click()
           self.wait.until(
               ec.presence_of_element_located((By.XPATH, locator.WebLocators().marriedLocator))).click()

           self.wait.until(ec.presence_of_element_located((By.XPATH, locator.WebLocators().conLocator))).click()
           self.wait.until(ec.presence_of_element_located((By.XPATH, locator.WebLocators().saveeLocator))).click()

       except NoSuchElementException as e:
           print(e)

       finally:
           self.quit()


obj = Empedit()
obj.login()


