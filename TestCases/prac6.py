import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

s = Service("C:\\Users\\aprat\\OneDrive\\Desktop\\selenium\\chromedriver98\\chromedriver.exe")
url = "https://diy.iiflinsurance.com/form/proposer-form?quote_id=Mr6ynrRUPktQJ8bHk1ix"
chrome_options = Options()
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()
driver.get(url)
time.sleep(10)
wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Full Name']"))).send_keys('Apratim Chaudhuri')
dob = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='date']")))
time.sleep(10)
driver.execute_script("arguments[0].value = arguments[1]", dob, "2004-03-18")
time.sleep(10)

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Male']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Email Id']"))).send_keys('ApratimChaudhuri@gmail.com')


wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Mobile Number']"))).send_keys('9789898989')
wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Mobile Number'])[2]"))).send_keys('9789898912')
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='NEXT']"))).click()