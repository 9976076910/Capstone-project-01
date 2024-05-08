#Capstone Project 01
#Valid and Invalid Login
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

class Orangehrm:

#Constructor
   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.wait = WebDriverWait(self.driver, 10)

#Boot Function
   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()
#Quit Function
   def quit(self):
       self.driver.quit()


#Method to enter text
   def enterText(self, locator, textvalue):
       element = self.wait.until(ec.presence_of_element_located((By.NAME,locator)))
       element.clear()
       element.send_keys(textvalue)

#Method to click Button
   def clickButton(self, locator):
       return self.wait.until(ec.presence_of_element_located((By.XPATH,locator))).click()

#Login Function to Orangehrm
   def login(self):
       try:
           self.boot()


           # For loop for reading the data


           for row in range(2, data.WebData().rowCount()+1):
               username = data.WebData().readData(row, 3)
               password = data.WebData().readData(row, 4)
           #Entering the data's
               self.enterText(locator.WebLocators().usernameLocator, username)
               self.enterText(locator.WebLocators().passLocator, password)
               self.clickButton(locator.WebLocators().subLocator)


               if self.driver.current_url == data.WebData().dashboardURL:
                   print("Successfully Loggedin")
                   data.WebData().writeData(row, 5, "PASSED")
                   self.clickButton(locator.WebLocators().buttonLocator)
                   self.clickButton(locator.WebLocators().logoutButton)
               else:
                    print("Login unsuccessfull")
                    data.WebData().writeData(row, 5, "FAILED")
       except NoSuchElementException as e:
            print(e)
       finally:
            self.quit()

obj = Orangehrm()
obj.login()
