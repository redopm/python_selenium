from selenium import webdriver
import time

driver =  webdriver.Firefox()
driver.get("https://selenium.dev/selenium/docs/api/java/")

driver.switch_to.frame("packageListFrame") # frame one to click 
driver.find_element_by_link_text("org.openqa.selenium").click() # link click in the  frame one 

time.sleep(3)

driver.switch_to.default_content() # this is for return  to main  page 
time.sleep(3)

driver.switch_to.frame("packageFrame") # frame two 
driver.find_element_by_link_text("Alert").click() # frame  two link click  
time.sleep(3)

driver.switch_to.default_content() # this is for return  to main  page 

driver.switch_to.frame("classFrame") # third frame 
driver.find_element_by_xpath('/html/body/div[1]/ul/li[5]/a').click()

driver.switch_to.default_content()# this is for return  to main  page 

driver.close()


