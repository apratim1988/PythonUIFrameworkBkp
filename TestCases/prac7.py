import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

s='./Chrome Driver/chromedriver.exe'

url = 'https://assisted.hellozindagi.co/home-page'
driver = webdriver.Chrome(executable_path=s)
driver.maximize_window()
driver.get(url)
time.sleep(3)
#page1
driver.find_element(By.XPATH, "//p[contains(text(),'2-Wheeler Insurance')]").click()
time.sleep(3)

#page2
driver.find_element(By.XPATH, "//input[@formcontrolname='regNo']").send_keys("DL01AB1234")
driver.find_element(By.XPATH, "//input[@formcontrolname='phone']").send_keys("9999999999")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(20)

#page3
driver.find_element(By.XPATH, "//input[@formcontrolname='owner_first_name']").send_keys("SURIYA")
driver.find_element(By.XPATH, "//input[@formcontrolname='owner_last_name']").send_keys("PRANAV")
driver.find_element(By.XPATH, "//input[@formcontrolname='vehicle']").click()
driver.find_element(By.XPATH, "//input[@role='combobox']").send_keys("B")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@role='combobox']").send_keys("AJ")
driver.find_element(By.XPATH, "//span[contains(text(),'BAJAJ')]").click()
driver.find_element(By.XPATH, "//input[@role='combobox']").send_keys("A")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@role='combobox']").send_keys("SPI")
driver.find_element(By.XPATH, "//span[contains(text(),'ASPIRE')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//p[contains(text(),'STANDARD')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//mat-select[@formcontrolname='manufacturing_year']").click()
driver.find_element(By.XPATH, "//span[contains(text(),'2018')]").click()
driver.find_element(By.XPATH,"(//button[@aria-label='Open calendar'])[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"(//button[@aria-label='Choose month and year'])").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[contains(text(),'2018')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[contains(text(),'JAN')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//td[@class='mat-calendar-body-cell mat-calendar-body-active ng-star-inserted']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//p[contains(text(),'Is active')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//mat-select[@formcontrolname='pre_name_of_insurer']").click()
time.sleep(1)
button = driver.find_element(By.XPATH,"//span[contains(text(),' Bajaj Allianz General Insurance Co. Ltd. ')]")
driver.execute_script("arguments[0].click();", button)
driver.find_element(By.XPATH,"(//button[@aria-label='Open calendar'])[2]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//td[@class='mat-calendar-body-cell mat-calendar-body-active ng-star-inserted']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@formcontrolname='pre_policy_number']").send_keys("123456789")
driver.find_element(By.XPATH,"(//label[contains(text(),'No')])").click()
driver.find_element(By.XPATH,"//label[contains(text(),'0%')]").click()

button = driver.find_element(By.XPATH, "//button[@type='submit']")
driver.execute_script("arguments[0].click();", button)

#page4
time.sleep(20)
driver.find_element(By.XPATH,"//div[p[contains(text(),'I declare that my')]]/div//img").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Confirm & Proceed ')]").click()
time.sleep(10)

#page5
driver.find_element(By.XPATH,"//input[@formcontrolname='proposar_email']").send_keys('abcd@abcd.com')
driver.find_element(By.XPATH,"//button[@aria-label='Open calendar']").click()
driver.find_element(By.XPATH,"//td[@class='mat-calendar-body-cell mat-calendar-body-active ng-star-inserted']").click()
driver.find_element(By.XPATH,"//input[@formcontrolname='address_1']").send_keys('abcd, abcd')
driver.find_element(By.XPATH,"//input[@formcontrolname='pincode']").send_keys('600001')
driver.find_element(By.XPATH,"//input[@formcontrolname='engine_number']").send_keys('123456')
driver.find_element(By.XPATH,"//input[@formcontrolname='chassis_number']").send_keys('11111111111111111')
driver.find_element(By.XPATH,"//input[@formcontrolname='nominee_fname']").send_keys('abcd')
driver.find_element(By.XPATH,"//input[@formcontrolname='nominee_lname']").send_keys('abcd')
driver.find_element(By.XPATH,"//input[@formcontrolname='nominee_age']").send_keys('30')
driver.find_element(By.XPATH,"//mat-select[@formcontrolname='nominee_relation']").click()
driver.find_element(By.XPATH,"//span[contains(text(),'Spouse')]").click()
driver.find_element(By.XPATH,"//div[p[contains(text(),'I confirm that')]]/div//img").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Confirm & Proceed')]").click()
time.sleep(10)

#page6
driver.find_element(By.XPATH,"//button[contains(text(),' Proceed & Buy')]").click()

