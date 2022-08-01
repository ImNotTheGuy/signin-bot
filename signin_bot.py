import date_and_time
import time
from jproperties import Properties

# Read from config file
configs = Properties()


with open('config.properties', 'rb') as config_file:
    configs.load(config_file)

USERNAME = configs.get("username").data
PASSWORD = configs.get("password").data


START_URL = "https://sign.m2iformation.fr/signin"

# STEP 1: LOGIN DETAILS

# username: id = inputPhoneNumber
# password: id = inputSmsCode
# connect:  id = connexion

# STEP 2: GO TO TIMESHEET

TIME_SHEET_URL = "https://sign.m2iformation.fr/timesheet"

# STEP 3: CLICK ON CURRENT DATE

# date-id-style: mm/dd/yyyyam or mm/dd/yyyypm

today_date = date_and_time.GetDate().today_date
am_or_pm = date_and_time.GetDate().am_or_pm

print(f"id is: {today_date + am_or_pm}")

date_time_id = today_date + am_or_pm

# STEP 4: VALIDATE AND DISCONNECT

DISCONNECT_URL = "https://sign.m2iformation.fr/close-session"


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get(START_URL)
driver.maximize_window()

driver.implicitly_wait(3)

username = driver.find_element_by_id("inputPhoneNumber")
username.send_keys(USERNAME)

driver.implicitly_wait(0.5)

password = driver.find_element_by_id("inputSmsCode")
password.send_keys(PASSWORD)

driver.implicitly_wait(0.5)

time.sleep(1)
    
login = driver.find_element_by_xpath('//*[@id="connexion"]')
login.click()

time.sleep(1)

print(driver.current_url)

driver.implicitly_wait(0.5)

time.sleep(2)

print(driver.current_url)

link_to_get = "https://sign.m2iformation.fr/timesheet"

links = driver.find_elements_by_tag_name("a")
for link in links:
    if link.get_attribute("href") == link_to_get:
        link.click()
        break



time.sleep(2)

print(driver.current_url)

sign = driver.find_element_by_id(date_time_id)
sign.click()

time.sleep(1)


link_to_get = "https://sign.m2iformation.fr/close-session"
links = driver.find_elements_by_tag_name("a")
for link in links:
    if link.get_attribute("href") == link_to_get:
        break

driver.get(link_to_get)


driver.implicitly_wait(0.5)


time.sleep(1)

driver.close()