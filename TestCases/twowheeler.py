import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s=Service("C:\\Users\\aprat\\OneDrive\\Desktop\\selenium\\chromedriver98\\chromedriver.exe")

#page1
url = "https://anandrathi.demo.riskcovry.com/partner/login"
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(url)
driver.find_element(By.NAME, "user_name").send_keys("9998887776")
driver.find_element(By.NAME, "password_name").send_keys("qwerty123")
driver.find_element(By.XPATH, "//button[@type= 'submit']").click()
time.sleep(3)
#page2
driver.find_element(By.XPATH, "//*[contains(text(),'2 Wheeler Insurance')]").click()
time.sleep(6)
#page3
driver.find_element(By.XPATH, "//button[@class='buyBtn pointer']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//img[@src='https://dssrylrxc4fuc.cloudfront.net/attachments/files/000/000/027/original/download.png?1633038024']").click()
driver.find_element(By.XPATH, "//button[contains(text(),'NEXT')]").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[name='brandTxt']").send_keys("xcd 135")
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(),'135')]").click()
driver.find_element(By.XPATH, "//button[contains(text(),'NEXT')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'135')]").click()
driver.find_element(By.XPATH, "//button[contains(text(),'NEXT')]").click()
time.sleep(3)
#page4
driver.find_element(By.XPATH, "//input[@id='mat-input-3']").send_keys("KA")
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(),'KA-1')]").click()
driver.find_element(By.XPATH, "//div[@class='rto_desktop']//button").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='mat-icon-button mat-button-base']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@aria-label='Choose month and year']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[contains(text(),'2018')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[contains(text(),'JAN')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[contains(text(),'10')]").click()
driver.find_element(By.XPATH, "//button[contains(text(),'NEXT')]").click()
time.sleep(3)
#page5
driver.find_element(By.XPATH, "//input[@placeholder='dd/ mm/ yyyy']").send_keys("15/4/2022")
# driver.find_element(By.XPATH, "//div[contains(@class,'noPadding policy-datepicker')]//button").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//button[@class='mat-calendar-period-button mat-button mat-button-base']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//td[@aria-label='2022']/div").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//div[contains(text(),'APR')]").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//div[contains(text(),'15')]").click()
driver.find_element(By.XPATH, "//button[contains(text(),'NEXT')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='Mobile Number']").send_keys("9836680067")
driver.find_element(By.XPATH, "//button[@class='submit-arrow']").click()
time.sleep(5)
#page6
driver.find_element(By.XPATH, "//span[contains(text(),'SHARE QUOTE')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='col-xs-12 col-md-12 col-lg-12 tab-style']//div[@class='col-sm-3 col-md-3 col-lg-3']//span//input").click()
time.sleep(1)
driver.execute_script("window.scrollTo(0,1900);")
time.sleep(1)
#height = driver.execute_script("return document.body.scrollHeight")
#print(height)
driver.find_element(By.XPATH, "//button[@class='nextBtn']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[contains(@class,'desktop_screen_only')]//input[@name='name']").send_keys("apratim chaudhuri")
driver.find_element(By.XPATH, "//div[contains(@class,'desktop_screen_only')]//input[@name='email']").send_keys("apra@gmail.com")
driver.find_element(By.XPATH, "//div[contains(@class,'desktop_screen_only')]//input[@name='phone_number']").send_keys("9836680067")
driver.find_element(By.XPATH, "//button[contains(@class,'nextBtn')]").click()
time.sleep(6)
driver.find_element(By.XPATH, "(//img[not (@class) and contains(@src,'royal_sundaram')]//ancestor::div[@class='ng-star-inserted']//button[@class='btn-m-orange'])[2]").click()
time.sleep(8)
driver.find_element(By.XPATH, "//div[@class='col-xs-4 col-md-4 col-lg-4 right-section']//button[contains(text(),'PROCEED')]").click()
time.sleep(3)
#page7
driver.find_element(By.XPATH, "//span[contains(text(),'Vehicle Registration Number')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("KA01J9077")
driver.find_element(By.XPATH, "//span[contains(text(),'Engine Number')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("AB12CD34")
driver.find_element(By.XPATH, "//span[contains(text(),'Chassis Number')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("APRATIM1234567CHA")
time.sleep(1)
driver.find_element(By.XPATH, "(//div[@class='mat-select-arrow-wrapper'])[1]").click()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='mat-option-text'])[2]"))))
driver.find_element(By.XPATH, "(//div[@class='mat-select-arrow-wrapper'])[2]").click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-option-text' and contains(text(),'Yes')]"))).click()
driver.find_element(By.XPATH, "//span[contains(text(),'What is your financer')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("Bajaj")
driver.find_element(By.XPATH, "(//div[@class='mat-select-arrow-wrapper'])[3]").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-option-text' and contains(text(),'Hire')]"))).click()
driver.find_element(By.XPATH, "(//div[@class='mat-select-arrow-wrapper'])[4]").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-option-text' and contains(text(),'Yes')]"))).click()
driver.find_element(By.XPATH, "//span[contains(text(),'PUC Number')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("12345")
driver.find_element(By.XPATH, "//span[contains(text(),'PUC Expiry')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("10/2/2023")
driver.find_element(By.XPATH, "(//div[@class='mat-select-arrow-wrapper'])[5]").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-option-text' and contains(text(),'United India Insurance')]"))).click()
driver.find_element(By.XPATH, "(//div[@class='mat-select-arrow-wrapper'])[6]").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-option-text' and contains(text(),'Comprehensive')]"))).click()
driver.find_element(By.XPATH, "//span[contains(text(),'Previous Policy Number')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("VMNS001300000100")
driver.find_element(By.XPATH, "//span[contains(text(),'Nominee Name')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("test")
driver.find_element(By.XPATH, "//span[contains(text(),'Nominee Age')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("30")
driver.find_element(By.XPATH, "(//div[@class='mat-select-arrow-wrapper'])[7]").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-option-text' and contains(text(),'Spouse')]"))).click()
driver.find_element(By.XPATH, "(//div[@class='mat-select-arrow-wrapper'])[8]").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-option-text' and contains(text(),'Driving')]"))).click()
driver.find_element(By.XPATH, "(//div[@class='mat-select-arrow-wrapper'])[9]").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='mat-option-text' and contains(text(),'Mr')])[1]"))).click()
driver.find_element(By.XPATH, "//span[.='Name']//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("Apratim Chaudhuri")
driver.find_element(By.XPATH, "(//div[@class='mat-select-arrow-wrapper'])[10]").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-option-text' and contains(text(),'Male')]"))).click()
driver.find_element(By.XPATH, "//span[contains(text(),'PAN')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("AMHPC9725D")
driver.find_element(By.XPATH, "//span[contains(text(),'Aadhar')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("896574523658")
driver.find_element(By.XPATH, "//span[contains(text(),'Address Line 1')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("GD")
driver.find_element(By.XPATH, "//span[contains(text(),'Address Line 2')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("FE")
driver.find_element(By.XPATH, "//span[contains(text(),'Pincode')]//ancestor::div[@class='col-xs-12 col-md-12 col-lg-12 ng-star-inserted']//input").send_keys("560008")
driver.execute_script("window.scroll(0, 0);")
time.sleep(5)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//button[contains(text(),' PROCEED ')])[2]"))).click()
time.sleep(7)
regn_no = driver.find_element(By.XPATH, "(//div[@class='col-xs-6 col-md-6 question-ans bold'])[2]").text
engg_no = driver.find_element(By.XPATH, "(//div[@class='col-xs-6 col-md-6 question-ans bold'])[3]").text
chss_no = driver.find_element(By.XPATH, "(//div[@class='col-xs-6 col-md-6 question-ans bold'])[4]").text
print(regn_no)
print(engg_no)
print(chss_no)
driver.find_element(By.XPATH, "(//button[contains(text(),'SHARE')])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@type='submit']").click()


