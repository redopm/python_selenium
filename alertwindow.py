from selenium import webdriver
import time 

driver =  webdriver.Firefox()

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()

time.sleep(5)

#driver.switch_to_alert().accept() # it is pressed ok button to accept the popup

driver.switch_to_alert().dismiss() # it is pressed cancle button to reject the popup

driver.close() # it is close the all open window

