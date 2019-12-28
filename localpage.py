from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("http://127.0.0.1/login.html")
#assert "Python" in driver.title
user_name = driver.find_element_by_name("uname")
user_name.clear()
user_name.send_keys("omp")
paswd = driver.find_element_by_name("psw")
paswd.clear()
paswd.send_keys("123456780")
butn = driver.find_element_by_xpath("/html/body/form/div[2]/button").click()

#assert "No results found." not in driver.page_source
#driver.close()
time.sleep(5)
driver.close()