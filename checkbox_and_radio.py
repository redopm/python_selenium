from selenium import webdriver


driver = webdriver.Firefox()

driver.get("http://www.demo.guru99.com/test/radio.html")

status = driver.find_element_by_id("vfb-7-1").is_selected()
print(status) # return the status of the radio button
status= driver.find_element_by_id("vfb-7-1").click()
print(status) # return the status of the radio button

status = driver.find_element_by_id("vfb-6-2").is_selected()
print(status)
driver.find_element_by_id("vfb-6-2").click()
driver.find_element_by_id("vfb-6-1").click()
driver.find_element_by_id("vfb-6-0").click()
driver.close()