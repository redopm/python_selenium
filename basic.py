from selenium import webdriver
#from selenium.webdriver.common.keys import key
import time 

driver = webdriver.Firefox()
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title) # return the title of page 
print(driver.current_url)# return corrent url of page 
#print(driver.page_source) # return html format page source 

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click() # click on button to open child page

time.sleep(10)
driver.close() # close the all window  insteed of current 
#driver.quit() #  close browser