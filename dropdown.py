from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()

driver.get("http://www.demo.guru99.com/V4/manager/addAccount.php")

driver.find_element(By.NAME, "cusid").send_keys("9462333028")
drop = driver.find_element(By.NAME, "selaccount")
element = Select(drop)
 
#element.select_by_visible_text("Savings") # select element by visible text

element.select_by_value("Current") #select element by value

#element.select_by_index("2") #select element by index

driver.find_element(By.NAME, "inideposit").send_keys("10000")
driver.find_element_by_name("button2").click

driver.quit()