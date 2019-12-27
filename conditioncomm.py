from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("http://www.demo.guru99.com/V4/index.php")
time.sleep(5)

user_ele = driver.find_elements_by_xpath("/html/body/form/table/tbody/tr[1]/td[2]/input").send_Keys("opm")
driver.quit() 
