from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("http://www.demo.guru99.com/V4/index.php")

user_ele = driver.find_element_by_name("uid")
user_ele.clear()
uname= user_ele.send_keys("mngr239293")
paswd = driver.find_element_by_name("password")
paswd.clear()
psw = paswd.send_keys("dAbUnUt")
driver.find_element_by_name("btnLogin").click()


#time.sleep(5)
driver.close()
