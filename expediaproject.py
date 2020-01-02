from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
import time 

driver = webdriver.Firefox()
driver.get("https://www.expedia.co.in/")

driver.implicitly_wait(5) # this is implecite wait 
driver.find_element(By.ID,"tab-flight-tab-hp").click()
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("NYC")
time.sleep(2)
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("SFO")
driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("10/01/2020")
driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("20/01/2020")
driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

wait = WebDriverWait(driver, 10) # this is explicite wait 
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
element.click()
time.sleep(3)
driver.close()

