import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# input your username and password here
user = "***"
pwd = "***"
datefrom = "2017-08-16"
dateto = "2018-08-23"

# You need to download chromedriver to your own directory
chromedriver = "YourDirectory/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("https://www.beds24.com/api/csv/getbookingscsv")
elem = driver.find_element_by_name("username")
elem.send_keys(user)
elem = driver.find_element_by_name("password")
elem.send_keys(pwd)
elem = driver.find_element_by_name("datefrom")
elem.clear()
elem.send_keys(datefrom)
elem = driver.find_element_by_name("dateto")
elem.clear()
elem.send_keys(dateto)
elem.send_keys(Keys.RETURN)
driver.close()
