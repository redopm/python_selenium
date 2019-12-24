from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Firefox()

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title) #forword

driver.get("https://www.wikipedia.org/")
print(driver.title)# backword
time.sleep(5)
driver.back()
print(driver.title)# forword
time.sleep(5)
driver.forward()
print(driver.title)# backword
driver.close()