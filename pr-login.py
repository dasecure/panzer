from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time



# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.
# , options=options

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")

# head to github login page
driver.get("https://www.panzerrush.com/?e=1")
print(driver.title)
# find username/email field and send the username itself to the input field
driver.find_element_by_id("loginname").send_keys(username)
# find password input field and insert password as well
driver.find_element_by_id("loginpass").send_keys(password)
# click login button
driver.find_element_by_id("bigbutton").click()

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements_by_class_name("flash-error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    driver.get("https://www.panzerrush.com/titanium.php")
    time.sleep(10)
    print(driver.current_url)
    # print(driver.title)
    # print(driver.find_element_by_css_selector("#hintbox > div:nth-child(1) > button:nth-child(5)"))
    print("[+] Login successful")

# URLs
# info about other users
# https://www.panzerrush.com/charts.php?a={username}&more=1
# info about self
# https://www.panzerrush.com/titanium.php
# battle report
# https://www.panzerrush.com/gold?b=3

driver.close()
