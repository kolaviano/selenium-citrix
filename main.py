from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
import time

chromedriver = "C:/Users/kolaviano/Downloads/myfirst/selenium-citrix/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("http://ctxadmin-pub.pc.factset.com/Director")

conn = sqlite3.connect('Citrix.db')
cursor = conn.execute("SELECT username, password, domain from users")

for row in cursor:
    driver.find_element_by_id("UserName").send_keys(row[0])
    driver.find_element_by_id("Password").send_keys(row[1])
    driver.find_element_by_id("Domain").send_keys(row[2])
    driver.find_element_by_id("Submit").click()
    try:
        banner = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "Failure"))
        )
        if banner.text == "You must enter valid credentials.":
            print("")
            print("...Log on failed")
    except:
        print("...Log on successful")
    time.sleep(2)
    driver.find_element_by_id("UserName").clear()
    driver.find_element_by_id("Password").clear()
    driver.find_element_by_id("Domain").clear()

conn.close()
driver.quit()