from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get("http://www.demo.guru99.com/V4/manager/Managerhomepage.php")

links = driver.find_elements_by_tag_name("a")
print(len(links))

for link in links:
    print(link.text)


# click on link by link text 

driver.find_element(By.LINK_TEXT, "Bank Project").click()
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, "Agil").click()

driver.close()