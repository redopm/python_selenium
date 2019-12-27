from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox('/home/omprakash/python_selenium/geckodriver-v0.26.0-linux64')

driver.get("http://www.demo.guru99.com/V4/index.php")
time.sleep(5)

driver.find_elements_by_name("uid").click

