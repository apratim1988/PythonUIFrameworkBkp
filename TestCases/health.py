import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
driver.find_element(By.XPATH, "//p[contains(text(),'Health Insurance')]").click()
time.sleep(3)
#page3
driver.find_element(By.XPATH, "//input[@placeholder='Where do you stay']").send_keys("560008")
dropdown = driver.find_element(By.XPATH, "//select[@formcontrolname = 'income']")

for option in dropdown.find_elements_by_tag_name('option'):
    value = option.text

driver.find_element(By.XPATH, "//input[@placeholder='How do we reach you']").send_keys("9836680067")
time.sleep(10)
sumdropdown = Select(driver.find_element(By.XPATH, "//select[@formcontrolname = 'income']"))
sumdropdown.select_by_visible_text("700000")
driver.find_element(By.XPATH, "//*[contains(text(),'keyboard_arrow_right')]").click()
time.sleep(6)
#page4
driver.find_element(By.XPATH, "//*[text()='Self']/following-sibling::mat-checkbox").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@placeholder='Enter Age']").send_keys("30")
time.sleep(2)
driver.find_element(By.XPATH, "//*[contains(text(),'keyboard_arrow_right')]").click()
time.sleep(6)
#page5
driver.find_element(By.XPATH, "//*[contains(text(),'Share Quotes')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='selectAll']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='btn custom-btn']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Please enter your name']").send_keys("Apratim Chaudhuri")
driver.find_element(By.XPATH, "//input[@placeholder='Enter your mail id']").send_keys("apratim.chaudhuri@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Enter your mobile number']").send_keys("9836680067")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//img[@type='button']").click()
time.sleep(2)
#page6
driver.execute_script("window.scrollTo(0,800);")
driver.find_element(By.XPATH, "//*[@class='outer outer-min-height']//*[contains(@src,'royal_sundaram')]//ancestor::div[@style='flex-direction: row; box-sizing: border-box; display: flex;']//div//button").click()
#page7
time.sleep(3)
driver.find_element(By.XPATH, "//p[@class='ng-star-inserted']").click()
time.sleep(3)
#page8
driver.find_element(By.XPATH, "//input[@formcontrolname='first_name']").send_keys("Apratim")
driver.find_element(By.XPATH, "//input[@formcontrolname='last_name']").send_keys("Chaudhuri")
driver.find_element(By.XPATH, "//input[@formcontrolname='dob']").send_keys("1/2/1992")
driver.find_element(By.XPATH, "//div[@class='mat-form-field-infix']//input[@formcontrolname='email']").send_keys("apratim.chaudhuri@gmail.com")
driver.find_element(By.XPATH, "//div[@class='mat-form-field-infix']//input[@formcontrolname='phone_number']").send_keys("9836680067")
driver.find_element(By.XPATH, "//input[@formcontrolname='annul_income']").send_keys("1000000")
driver.find_element(By.XPATH, "//input[@formcontrolname='pan_number']").send_keys("AMHPC9725D")
driver.find_element(By.XPATH, "//*[@formcontrolname='occupation']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(),'Salaried')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@formcontrolname='designation']").send_keys("QA")
driver.find_element(By.XPATH, "//*[@formcontrolname='marital_status']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()=' Single ' and @class='mat-option-text']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@formcontrolname='educational_qualification']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()=' Graduate ' and @class='mat-option-text']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@formcontrolname='tpa_name']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()=' Medi Assist Insurance (TPA) Pvt Ltd ' and @class='mat-option-text']").click()
driver.find_element(By.XPATH, "//*[@formcontrolname='building_name']").send_keys("GD")
driver.find_element(By.XPATH, "//input[@formcontrolname='area']").send_keys("SaltLake")
time.sleep(2)
driver.find_element(By.XPATH, "//p[@class='ng-star-inserted']").click()
time.sleep(4)
#page9
driver.find_element(By.XPATH, "//input[@formcontrolname='first_name']").send_keys("Apratim")
driver.find_element(By.XPATH, "//input[@formcontrolname='last_name']").send_keys("Chaudhuri")
driver.find_element(By.XPATH, "//input[@formcontrolname='dob']").send_keys("1/2/1992")
driver.find_element(By.XPATH, "//mat-card[@class='form-bg mat-card ng-star-inserted']/div/div/div/div//div[@class='row']//div[@class='col-md-6']/mat-radio-group//mat-radio-button[@value='male']").click()
driver.find_element(By.XPATH, "//input[@formcontrolname='height']").send_keys("180")
driver.find_element(By.XPATH, "//input[@formcontrolname='weight']").send_keys("70")
driver.find_element(By.XPATH, "//input[@formcontrolname='designation']").send_keys("QA")
driver.find_element(By.XPATH, "//input[@formcontrolname='nominee_first_name']").send_keys("test")
driver.find_element(By.XPATH, "//input[@formcontrolname='nominee_last_name']").send_keys("test")
driver.find_element(By.XPATH, "//input[@formcontrolname='nominee_dob']").send_keys("2/2/1992")
driver.find_element(By.XPATH, "//mat-card[@class='form-bg mat-card']/div/div//div[@class='row']//div[@class='col-md-6']/mat-radio-group//mat-radio-button[@value='female']").click()
driver.find_element(By.XPATH, "//*[@formcontrolname='nominee_relation']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()=' Wife ' and @class='mat-option-text']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//p[@class='ng-star-inserted']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//p[@class='ng-star-inserted']").click()
time.sleep(7)
#page10
name = driver.find_element(By.XPATH, "//div[@class='col-12 col-md-4']/h5").text
phone = driver.find_element(By.XPATH, "//div[@class='col-12 col-md-3']/h5").text
email = driver.find_element(By.XPATH, "//div[@class='col-12 col-md-5']/h5").text
driver.find_element(By.XPATH, "//*[contains(text(),' Send to Customer')]").click()
time.sleep(3)








