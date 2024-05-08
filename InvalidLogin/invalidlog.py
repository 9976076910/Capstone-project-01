# Invalid login to OrangeHRM portal
from Value import values
from Identifiers import identifier


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




class LoginPage:


   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.wait = WebDriverWait(self.driver, 10)


   def boot(self):
       self.driver.get(values.WebData().url)
       self.driver.maximize_window()




   def quit(self):
       self.driver.quit()


   def invalidlogin(self):
       try:
           self.boot()



           self.wait.until(ec.presence_of_element_located((By.NAME, identifier.WebLocators().usernameLocator))).send_keys(
               values.WebData().username)
           self.wait.until(ec.presence_of_element_located((By.NAME, identifier.WebLocators().passwordLocator))).send_keys(
               values.WebData().password)
           self.wait.until(ec.presence_of_element_located((By.XPATH, identifier.WebLocators().buttonLocator))).click()
           #self.wait.until(ec.presence_of_element_located((By.XPATH, identifier.WebLocators().msgLocator)))



           if self.driver.current_url == values.WebData().dashboardURL:
               print(" Success")
           else:
               print("Invalid credentials")


       except NoSuchElementException as e:
           print(e)
       finally:
           self.quit()




obj = LoginPage()
obj.invalidlogin()