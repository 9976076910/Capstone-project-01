#code to delete the existing user
from Data import data
from Locators import locator


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class Empdelete:

# Constructor
   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.wait = WebDriverWait(self.driver, 10)

#Boot Function
   def boot(self):
       self.driver.get(data.WebDatas().url)
       self.driver.maximize_window()

   def quit(self):
       self.driver.quit()

   def login(self):
       try:
           self.boot()
           #This will scroll the Webpage
           self.driver.execute_script('window.scrollBy(0, 800)')
           #Used to Locate and send the Username
           self.wait.until(ec.presence_of_element_located((By.NAME, locator.WebLocators().usernameLocator))).send_keys(
               data.WebDatas().username)
           #Used to locate and send the Password
           self.wait.until(ec.presence_of_element_located((By.NAME, locator.WebLocators().passLocator))).send_keys(
               data.WebDatas().password)
           #Login
           self.wait.until(ec.presence_of_element_located((By.XPATH, locator.WebLocators().subLocator))).click()
           self.driver.execute_script('window.scrollBy(0, 800)')
           #Clicking PIM
           self.wait.until(ec.presence_of_element_located((By.XPATH, locator.WebLocators().pimLocator))).click()
          #deleting an existing user
           self.wait.until(ec.presence_of_element_located((By.XPATH, locator.WebLocators().deleteLocator))).click()
          #Confirming the alert Msg
           self.wait.until(ec.presence_of_element_located((By.XPATH, locator.WebLocators().alertLocator))).click()

       except NoSuchElementException as e:
           print(e)

       finally:
           self.quit()

obj = Empdelete()
obj.login()


