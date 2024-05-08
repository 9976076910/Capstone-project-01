from Data import data
from Locator import locators


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep


# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




class EmpAdd:


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



           self.wait.until(ec.presence_of_element_located((By.NAME, locators.WebLocators().usernameLocator))).send_keys(
               data.WebDatas().username)
           self.wait.until(ec.presence_of_element_located((By.NAME, locators.WebLocators().passLocator))).send_keys(
               data.WebDatas().password)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().subLocator))).click()
           self.wait.until(
               ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimLocator))).click()

           self.wait.until(
               ec.presence_of_element_located((By.XPATH, locators.WebLocators().addLocator))).click()
           self.wait.until(
               ec.presence_of_element_located((By.NAME, locators.WebLocators().firstnameLocator))).send_keys(
               data.WebDatas().firstname)
           self.wait.until(ec.presence_of_element_located((By.NAME, locators.WebLocators().LastnameLocator))).send_keys(
               data.WebDatas().lastName)

           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().saveLocator))).click()

           self.driver.execute_script('window.scrollBy(0, 800)')
           add = self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().conLocator)))
           self.driver.execute_script("arguments[0].click();", add)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().buttonLocator))).click()
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().submitLocator))).click()
           self.driver.execute_script('window.scrollBy(0, 800)')



       except NoSuchElementException as e:
           print(e)

       finally:
           self.quit()






obj = EmpAdd()
obj.login()


