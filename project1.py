from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.demo.guru99.com/V4/index.php") # after this wait for varification
driver.implicitly_wait(5) # wait for 10 seconds 
assert "Guru99 Bank" in driver.title # varify the title of the page 
# implecit wait for all element of page 
driver.find_element_by_name("uid").send_keys("mngr239293") 
driver.find_element_by_name("password").send_keys("dAbUnUt")
driver.find_element_by_name("btnLogin").click()

#wait = WebDriverWait(driver, 10)
time.sleep(3)
driver.find_element_by_link_text("New Customer").click()
#time.sleep(2)
status = driver.find_element(By.NAME, "name").is_displayed()
print(status)
driver.find_element(By.NAME, "name").send_keys("omprakash maury")
driver.find_element(By.NAME, "rad1").click()
radio = driver.find_element(By.NAME, "rad1").is_enabled()
print(radio)
#driver.find_element(By.NAME, "dob").clear()
driver.find_element(By.ID, "dob").send_keys("20/08/1996")
driver.find_element(By.NAME, "addr").send_keys("vill -narayanpur, post-mairhi, dist- chandauli 232104")
driver.find_element(By.NAME, "city").send_keys("chandauli")
driver.find_element(By.NAME, "state").send_keys("utter pradesh")
driver.find_element(By.NAME, "pinno").send_keys("232104")
driver.find_element(By.NAME, "telephoneno").send_keys("9462333028")
driver.find_element(By.NAME, "emailid").send_keys("opmaury001@gmail.com")
driver.find_element(By.NAME, "password").send_keys("omprakash")
driver.find_element(By.NAME, "sub").click()
time.sleep(10)
driver.close()